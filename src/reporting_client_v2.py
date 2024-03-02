import sys
import grpc
import reporting_pb2_grpc
import reporting_pb2
from pydantic import BaseModel, model_validator
from google.protobuf import json_format


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
        except ValueError:
            pass


def check_args(args: list) -> None:
    number_args = len(args)
    if number_args != 7:
        print('Invalid number of parameters')
    else:
        main(args)


if __name__ == '__main__':
    check_args(sys.argv)
