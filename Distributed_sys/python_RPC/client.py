import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.pow(2, 3))
print(s.add(2, 3))
print(s.mul(5, 2))

print(s.system.listMethods())

