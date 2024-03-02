# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import reporting_pb2 as reporting__pb2


class ReportingServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetReport = channel.unary_stream(
                '/reporting.ReportingServer/GetReport',
                request_serializer=reporting__pb2.Coordinates.SerializeToString,
                response_deserializer=reporting__pb2.Spaceship.FromString,
                )


class ReportingServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetReport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReportingServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetReport': grpc.unary_stream_rpc_method_handler(
                    servicer.GetReport,
                    request_deserializer=reporting__pb2.Coordinates.FromString,
                    response_serializer=reporting__pb2.Spaceship.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reporting.ReportingServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReportingServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/reporting.ReportingServer/GetReport',
            reporting__pb2.Coordinates.SerializeToString,
            reporting__pb2.Spaceship.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
