import client_side_connection
import peer_ip
import network_protocol
import random
	
def ask_question(peer_name):

	print('What host would you like to ask the question of?')
	host_input = input()
	host_location = None
	# Look up the host location in the peer_ip map
	for hostname, host in peer_ip.peer_map.items():
		name = str(eval(hostname)[4][0][1])
		if(host_input == name):
			host_location = host
	if(host_location == None):
		print("Host not found")
		return

	yesNum = str(random.random())
	noNum = str(random.random())

	#Question string should not have any network_protocol.SEPARATOR in it. (No semicolons)
	question = "Am I invited to the party?"
	print("Asking", question)

	# Connect to the appropriate host
	net = client_side_connection.ClientSideConnection(
		peer_name = peer_name, ip = host_location[0], portno = int(host_location[1]))

	net.send('Query')
	queryString = question + network_protocol.SEPARATOR + yesNum + network_protocol.SEPARATOR + noNum
	net.send(queryString)

	# print the response
	answer = net.recv()
	if(answer == yesNum):
		print(question, "->", "Yes")
	elif(answer == noNum):
		print(question, "->", "No")
	else:
		print("Something went wrong")

	net.done()