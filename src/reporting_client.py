import sys
import grpc
import reporting_pb2_grpc
import reporting_pb2
from google.protobuf import json_format


def main(args: list) -> None:
    channel = grpc.insecure_channel('localhost:8888')
    stub = reporting_pb2_grpc.ReportingServerStub(channel)
    coordinates = reporting_pb2.Coordinates(
        h=args[1], m=args[2], s=args[3],
        d=args[4], dm=args[5], ds=args[6]
    )
    reports = stub.GetReport(coordinates)
    for report in reports:
        print(json_format.MessageToDict(report))


def check_args(args: list) -> None:
    number_args = len(args)
    if number_args != 7:
        print('Invalid number of parameters')
    else:
        main(args)


if __name__ == '__main__':
    check_args(sys.argv)
