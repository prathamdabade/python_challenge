import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

#print(server.system.listMethods())
#print(server.system.methodHelp("phone"))

print(server.phone("Bert"))

#Bert is evil from evil4.jpg which is txt
