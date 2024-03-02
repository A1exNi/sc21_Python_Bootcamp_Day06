import sys
import grpc
import reporting_pb2_grpc
import reporting_pb2
from pydantic import BaseModel, model_validator
from google.protobuf import json_format
from sqlalchemy import (
    create_engine, Integer, String, Float, Boolean, Column, ForeignKey, func
)
from sqlalchemy.orm import Session, declarative_base, relationship


Base = declarative_base()
link_to_serverSQL = 'postgresql://ilanadah:ilanadah@localhost/dbspaceships'


class TraitorsSQL(Base):
    __tablename__ = 'traitors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    rank = Column(String)

    def __repr__(self):
        return '{"first_name": "%s", "last_name": "%s", "rank": "%s"}' % (
            self.first_name, self.last_name, self.rank
        )


class OfficerSQL(Base):
    __tablename__ = "officers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    rank = Column(String)
    spaceship_id = Column(Integer, ForeignKey('spaceships.id'))
    spaceship = relationship('SpaceshipSQL', back_populates='officers')

    def __repr__(self):
        return f"Officer(id={self.id!r}, \
            first_name={self.first_name!r}, \
            last_name={self.last_name!r}, \
            rank={self.rank!r}, \
            spaceship_id={self.spaceship_id!r})"


class SpaceshipSQL(Base):
    __tablename__ = "spaceships"
    id = Column(Integer, primary_key=True)
    alignment = Column(Integer)
    name = Column(String)
    ship_class = Column(Integer)
    length = Column(Float)
    crew_size = Column(Integer)
    armed = Column(Boolean)
    officers = relationship(
        'OfficerSQL',
        order_by=OfficerSQL.id,
        back_populates='spaceship'
    )

    def __repr__(self):
        return f"Spaceship(id={self.id!r}, \
            alignment={self.alignment!r}, \
            name={self.name!r}, \
            ship_class={self.ship_class!r}, \
            length={self.length!r}, \
            crew_size={self.crew_size!r}, \
            armed={self.armed!r}, \
            alignment={self.alignment!r})"


class Spaceship(BaseModel):
    alignment: int
    name: str
    ship_class: int
    length: float
    crew_size: int
    armed: bool

    @model_validator(mode='after')
    def validate_length(self):
        if self.ship_class == 0 and (
            self.length < 80 or self.length > 250 or self.crew_size < 4 or
            self.crew_size > 10
        ):
            raise ValueError('0')
        if self.ship_class == 1 and (
            self.length < 300 or self.length > 600 or self.crew_size < 10 or
            self.crew_size > 15 or self.alignment == 1
        ):
            raise ValueError('1')
        if self.ship_class == 2 and (
            self.length < 500 or self.length > 1000 or
            self.crew_size < 15 or self.crew_size > 30
        ):
            raise ValueError('2')
        if self.ship_class == 3 and (
            self.length < 800 or self.length > 2000 or
            self.crew_size < 50 or self.crew_size > 80 or self.alignment == 1
        ):
            raise ValueError('3')
        if self.ship_class == 4 and (
            self.length < 1000 or self.length > 4000 or
            self.crew_size < 120 or self.crew_size > 250 or self.armed
        ):
            raise ValueError('4')
        if self.ship_class == 5 and (
            self.length < 5000 or self.length > 20000 or
            self.crew_size < 300 or self.crew_size > 500
        ):
            raise ValueError('5')
        if self.alignment == 0 and self.name == 'Unknown':
            raise ValueError('Unknown ship')
        return self


def same_spaceship(officers, session, spaceship_id) -> bool:
    answer = True
    for officer in officers:
        for instance in session.query(OfficerSQL).filter(
            OfficerSQL.spaceship_id == spaceship_id
        ):
            if (
                officer.first_name != instance.first_name or
                officer.last_name != instance.last_name or
                officer.rank != instance.rank
            ):
                answer = False
                break
        if answer:
            break
    return answer


def save_in_sql(report):
    engine = create_engine(link_to_serverSQL)
    with Session(engine) as session:
        add_spaceship = True
        for instance in session.query(SpaceshipSQL).order_by(SpaceshipSQL.id):
            if instance.name == report.name:
                add_spaceship = not same_spaceship(
                    report.officers, session, instance.id
                )
                if not add_spaceship:
                    break
        if add_spaceship:
            new_spaceship = SpaceshipSQL(
                alignment=report.alignment,
                name=report.name,
                ship_class=report.ship_class,
                length=report.length,
                crew_size=report.crew_size,
                armed=report.armed
            )
            for officer in report.officers:
                new_spaceship.officers.append(
                    OfficerSQL(
                        first_name=officer.first_name,
                        last_name=officer.last_name,
                        rank=officer.rank
                    )
                )
            session.add(new_spaceship)
            session.commit()


def main(args: list) -> None:
    channel = grpc.insecure_channel('localhost:8888')
    stub = reporting_pb2_grpc.ReportingServerStub(channel)
    coordinates = reporting_pb2.Coordinates(
        h=args[1], m=args[2], s=args[3],
        d=args[4], dm=args[5], ds=args[6]
    )
    reports = stub.GetReport(coordinates)
    for report in reports:
        try:
            Spaceship(
                alignment=report.alignment,
                name=report.name,
                ship_class=report.ship_class,
                length=report.length,
                crew_size=report.crew_size,
                armed=report.armed
            )
            print('\t', json_format.MessageToDict(report))
            save_in_sql(report)
        except ValueError:
            pass


def is_traitor(alligment_officer: list) -> bool:
    answer = False
    s = sum(alligment_officer)
    if s > 0 and s != len(alligment_officer):
        answer = True
    return answer


def is_in_traitor(officer, session) -> bool:
    answer = False
    for traitor in session.query(TraitorsSQL):
        if (
            officer.first_name == traitor.first_name and
            officer.last_name == traitor.last_name and
            officer.rank == traitor.rank
        ):
            answer = True
            break
    return answer


def search_traitors():
    engine = create_engine(link_to_serverSQL)
    with Session(engine) as session:
        for officer in session.query(
            OfficerSQL.first_name,
            OfficerSQL.last_name,
            OfficerSQL.rank
        ).group_by(
            OfficerSQL.first_name,
            OfficerSQL.last_name,
            OfficerSQL.rank
        ).having(func.count(OfficerSQL.spaceship_id) > 1):
            alligment_officer = list()
            for instance2 in session.query(OfficerSQL):
                if (
                    officer.first_name == instance2.first_name and
                    officer.last_name == instance2.last_name and
                    officer.rank == instance2.rank
                ):
                    for spaceship in session.query(SpaceshipSQL).where(
                        SpaceshipSQL.id == instance2.spaceship_id
                    ):
                        alligment_officer.append(spaceship.alignment)
            if (
                is_traitor(alligment_officer) and
                not is_in_traitor(officer, session)
            ):
                new_traitor = TraitorsSQL(
                    first_name=officer.first_name,
                    last_name=officer.last_name,
                    rank=officer.rank
                )
                session.add(new_traitor)
                session.commit()


def print_traitors():
    engine = create_engine(link_to_serverSQL)
    with Session(engine) as session:
        for instatnce in session.query(TraitorsSQL):
            print(instatnce)


def check_args(args: list) -> None:
    number_args = len(args)
    if number_args > 8 and number_args < 2:
        print('Invalid number of parameters')
    elif number_args == 8 and args[1] == 'scan':
        search_traitors()
    elif number_args == 2 and args[1] == 'list_traitors':
        print_traitors()
    elif number_args == 7:
        main(args)
    else:
        print('Invalid parameters')


if __name__ == '__main__':
    check_args(sys.argv)
