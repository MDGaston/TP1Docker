# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import id_pb2 as id__pb2


class IdServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetId = channel.unary_unary(
                '/example.IdService/GetId',
                request_serializer=id__pb2.Empty.SerializeToString,
                response_deserializer=id__pb2.Id.FromString,
                )


class IdServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IdServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetId,
                    request_deserializer=id__pb2.Empty.FromString,
                    response_serializer=id__pb2.Id.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'example.IdService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IdService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/example.IdService/GetId',
            id__pb2.Empty.SerializeToString,
            id__pb2.Id.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
