from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import queue

container = queue.Queue()

def send(sender_name, file_name, file_type, binary_data):

    saved_file_path = "server_file_db/{}_{}.{}".format(sender_name, file_name, file_type)
    
    with open(saved_file_path, "wb") as handle:
        handle.write(binary_data.data)
        handle.close()
        container.put(saved_file_path)

def receive():
    with open(container.get(), "rb") as handle:
        return xmlrpc.client.Binary(handle.read())



server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)

print("Listening on port 8000...")

server.register_function(send, 'send')
server.register_function(receive, 'receive')

server.serve_forever()