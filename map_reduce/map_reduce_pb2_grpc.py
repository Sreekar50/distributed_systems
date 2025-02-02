# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import map_reduce_pb2 as map__reduce__pb2


class MapperStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Map = channel.unary_unary(
                '/map_reduce.Mapper/Map',
                request_serializer=map__reduce__pb2.MapRequest.SerializeToString,
                response_deserializer=map__reduce__pb2.MapResponse.FromString,
                )
        self.GetPartitionData = channel.unary_unary(
                '/map_reduce.Mapper/GetPartitionData',
                request_serializer=map__reduce__pb2.ReducerRequest.SerializeToString,
                response_deserializer=map__reduce__pb2.PartitionData.FromString,
                )


class MapperServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Map(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPartitionData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MapperServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Map': grpc.unary_unary_rpc_method_handler(
                    servicer.Map,
                    request_deserializer=map__reduce__pb2.MapRequest.FromString,
                    response_serializer=map__reduce__pb2.MapResponse.SerializeToString,
            ),
            'GetPartitionData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPartitionData,
                    request_deserializer=map__reduce__pb2.ReducerRequest.FromString,
                    response_serializer=map__reduce__pb2.PartitionData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'map_reduce.Mapper', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mapper(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Map(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/map_reduce.Mapper/Map',
            map__reduce__pb2.MapRequest.SerializeToString,
            map__reduce__pb2.MapResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPartitionData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/map_reduce.Mapper/GetPartitionData',
            map__reduce__pb2.ReducerRequest.SerializeToString,
            map__reduce__pb2.PartitionData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ReducerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Reduce = channel.unary_unary(
                '/map_reduce.Reducer/Reduce',
                request_serializer=map__reduce__pb2.ReducerRequest.SerializeToString,
                response_deserializer=map__reduce__pb2.ReduceResponse.FromString,
                )


class ReducerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Reduce(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReducerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Reduce': grpc.unary_unary_rpc_method_handler(
                    servicer.Reduce,
                    request_deserializer=map__reduce__pb2.ReducerRequest.FromString,
                    response_serializer=map__reduce__pb2.ReduceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'map_reduce.Reducer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Reducer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Reduce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/map_reduce.Reducer/Reduce',
            map__reduce__pb2.ReducerRequest.SerializeToString,
            map__reduce__pb2.ReduceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
