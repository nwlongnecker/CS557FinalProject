import parse_params
import server_side_connection
import server_methods

peer_name = parse_params.getUsername(server_side = True)

net = server_side_connection.ServerSideConnection(
	peer_name = peer_name)

print('Server Started, Waiting for connections...')

while True:
	net.nextConnection()

	command = net.recv()

	if(command == 'Query'):
		server_methods.answerQuestion(peer_name, net)

	net.done()
