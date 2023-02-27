import sys

import bsonrpc
import gevent.socket as gsocket
from bsonrpc import JSONRpc, ThreadingModel

from server.ServiceHandler import ServiceHandler


def main(argv):
    # Bind JSON-RPC server to the given port
    port = int(sys.argv[1])
    ss = gsocket.socket(gsocket.AF_INET, gsocket.SOCK_STREAM)
    ss.bind(('localhost', port))
    ss.listen(10)

    # Start JSON-RPC server
    print("Server running at port " + str(port) + "...")
    serviceHandler: ServiceHandler = ServiceHandler()
    while True:
        s, _ = ss.accept()
        JSONRpc(s, serviceHandler, framing_cls=bsonrpc.JSONFramingNone,
                threading_model=ThreadingModel.GEVENT, concurrent_request_handling=ThreadingModel.GEVENT)


if __name__ == '__main__':
    main(sys.argv)
