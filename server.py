import parse_params
import server_side_connection
import server_methods

peer_name = parse_params.getUsername(server_side = True)

user_password = parse_params.getPassword()
net = server_side_connection.ServerSideConnection(peer_name = peer_name, password = user_password)

print("Server {0} Started, Waiting for connections...".format(peer_name))

while True:
	net.nextConnection()

	command = net.recv()

	if(command == 'Query'):
		server_methods.answerQuestion(peer_name, net, user_password)
	elif(command == 'Gimme_yo_data'):
		server_methods.sendData(peer_name, net)

	net.done()
