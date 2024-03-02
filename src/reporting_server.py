import reporting_pb2
import reporting_pb2_grpc
import grpc
from concurrent import futures
from google.protobuf import json_format
from random import randint, random
import sys


class ReportingServerServicer(reporting_pb2_grpc.ReportingServerServicer):
    def GetReport(self, request, context):
        print('------------------------------------')
        if self.check_coordinates(request):
            print('=============================================')
            for i in range(randint(1, 10)):
                report = self.gen_report()
                print('\t', json_format.MessageToDict(report))
                yield report

    def check_coordinates(self, request) -> bool:
        answer = False
        if (
            request.h == '17' and request.m == '45' and
            request.s == '40.0409' and request.d == '-29' and
            request.dm == '00' and request.ds == '28.118'
        ):
            answer = True
        return answer

    def gen_report(self) -> reporting_pb2.Spaceship:
        spaceship_names = [
            'Enterprise', 'White Star', 'Star Destroyer',
            'Lexx', 'TET', 'Elysium', 'The Death Star',
            'Galaxy', 'Prometheus', 'Nostromo',
            'Millennium Falcon', 'TARDIS', 'Unknown'
        ]
        first_names = [
            'Christopher', 'Jean-Luc', 'William', 'Edward', 'Keiran',
            'Diana',       'Sarah',    'Reg',     'Leland', 'Tasha'
        ]
        last_names = [
            'Pike', 'Picard',  'Riker', 'Jellicoe', 'McDuff', 'Troy',
            'McDougle', 'Barclay', 'Lynch', 'Yar'
        ]
        ranks = [
            'Grand Admiral', 'High Admiral',
            'Admiral', 'Captain', 'Lieutenant', 'Cadet'
        ]
        report = reporting_pb2.Spaceship()
        report.alignment = randint(0, 1)
        report.ship_class = randint(0, 5)
        report.length = random() * 20000
        report.crew_size = randint(4, 500)
        report.armed = randint(0, 1)
        if report.alignment == reporting_pb2.Spaceship().Enemy:
            number_officers = randint(0, 10)
            report.name = spaceship_names[randint(0, len(spaceship_names)-1)]
        else:
            number_officers = randint(1, 10)
            report.name = spaceship_names[randint(0, len(spaceship_names)-2)]
        for _ in range(number_officers):
            officer = report.officers.add()
            officer.first_name = first_names[randint(0, len(first_names)-1)]
            officer.last_name = last_names[randint(0, len(last_names)-1)]
            officer.rank = ranks[randint(0, len(ranks)-1)]
        return report


class ReportingServerServicerTest(ReportingServerServicer):
    def gen_report(self) -> reporting_pb2.Spaceship:
        report = reporting_pb2.Spaceship()
        report.alignment = 1
        report.name = 'TET'
        report.ship_class = 0
        report.length = 100
        report.crew_size = 10
        report.armed = 0
        officer = report.officers.add()
        officer.first_name = 'Christopher'
        officer.last_name = 'Pike'
        officer.rank = 'Grand Admiral'
        return report


def serv(test_server: bool):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    if test_server:
        reporting_pb2_grpc.add_ReportingServerServicer_to_server(
            ReportingServerServicerTest(), server
        )
    else:
        reporting_pb2_grpc.add_ReportingServerServicer_to_server(
            ReportingServerServicer(), server
        )
    server.add_insecure_port("[::]:8888")
    server.start()
    server.wait_for_termination()


def check_args(args: list) -> None:
    number_args = len(args)
    if number_args > 2:
        print('Invalid number of parameters')
    elif number_args == 1:
        serv(False)
    else:
        serv(True)


if __name__ == '__main__':
    check_args(sys.argv)
