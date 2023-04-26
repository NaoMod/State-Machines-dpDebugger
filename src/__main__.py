import argparse
import sys

import bsonrpc
import gevent.socket as gsocket
from bsonrpc import JSONRpc, ThreadingModel

from server.ServiceHandler import ServiceHandler


def main(argv):
    parser = argparse.ArgumentParser(
        prog='State Machines Runtime',
        description='JSON-RPC runtime for a State Machines DSL')

    parser.add_argument('port', type=int, help='port at which the server should listen')
    parser.add_argument('-d', '--docker', action='store_true', help='whether this program is launched in a Docker container.')
    args = parser.parse_args()

    # Bind JSON-RPC server to the given port
    ss = gsocket.socket(gsocket.AF_INET, gsocket.SOCK_STREAM)
    ss.bind(('localhost', args.port))
    ss.listen(10)

    # Start JSON-RPC server
    print("Server running at port " + str(args.port) + "...")
    serviceHandler: ServiceHandler = ServiceHandler(args.docker)
    while True:
        s, _ = ss.accept()
        JSONRpc(s, serviceHandler, framing_cls=bsonrpc.JSONFramingNone,
                threading_model=ThreadingModel.GEVENT, concurrent_request_handling=ThreadingModel.GEVENT)


if __name__ == '__main__':
    main(sys.argv)
