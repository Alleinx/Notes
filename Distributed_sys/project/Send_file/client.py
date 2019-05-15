import xmlrpc.client

save_path = 'receive/'
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

with open("Nasa.jpg", "rb") as handle:
    proxy.send('Tester', 'Universe', 'jpg', xmlrpc.client.Binary(handle.read()))
    print('Sending file')

    handle.close()
    print('Send complete.')



with open(save_path + "Received_from_server.jpg", "wb") as handle:
    print('Receiving file')
    handle.write(proxy.receive().data)
    
    handle.close()
    print('Receive complete.')

