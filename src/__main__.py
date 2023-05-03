import argparse

import bsonrpc
import gevent.socket as gsocket
from bsonrpc import JSONRpc, ThreadingModel

from server.ServiceHandler import ServiceHandler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='State Machines Runtime',
        description='JSON-RPC runtime for a State Machines DSL')

    parser.add_argument(
        'port', type=int, help='port at which the server should listen')
    args = parser.parse_args()

    # Bind JSON-RPC server to the given port
    ss = gsocket.socket(gsocket.AF_INET, gsocket.SOCK_STREAM)
    ss.bind(('localhost', args.port))
    ss.listen(10)

    # Start JSON-RPC server
    print("Server running at port " + str(args.port) + "...")
    serviceHandler: ServiceHandler = ServiceHandler()
    while True:
        s, _ = ss.accept()
        JSONRpc(s, serviceHandler, framing_cls=bsonrpc.JSONFramingNone,
                threading_model=ThreadingModel.GEVENT, concurrent_request_handling=ThreadingModel.GEVENT)
