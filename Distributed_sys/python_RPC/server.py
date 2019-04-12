from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_path = ('/RPC', )

with SimpleXMLRPCServer(('localhost', 8000), requestHandler = RequestHandler) as server:
    print('Server waiting...')
    server.register_introspection_functions()

    server.register_function(pow)

    def add_function(x, y):
        return x + y

    server.register_function(add_function, 'add')

    class MyFuncs:
        def mul(self, x, y):
            return x * y

    server.register_instance(MyFuncs())

    server.serve_forever()
