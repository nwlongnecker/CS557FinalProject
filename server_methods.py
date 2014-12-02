import server_side_connection
import network_protocol
import random
import party_policy
import peer_ip
import client_methods

def answerQuestion(peer_name, net):
	queryString = net.recv();
	queryList = queryString.split(network_protocol.SEPARATOR)
	print(queryList)

	# If the answer is yes, send the yes number, otherwise send the no number
	if(solve(peer_name, queryList[0])):
		net.send(queryList[1])
	else:
		net.send(queryList[2])

def solve(peer_name, query):

	# Can I answer this question?
	if(party_policy.canAnswer(query)):
		body = party_policy.getBody(query)
		return solveBody(body)
	elif(party_policy.trustSomeone(query)):
		return phoneAFriend(peer_name, query)
	else:
		return False;

def solveBody(body):
	# Assuming all joins are ands
	isTrue = True
	for statement in body:
		isTrue = isTrue and statement #solve(statement)
	return isTrue

def phoneAFriend(peer_name, query):
	host_input = "Jane"
	host_location = None
	# Look up the host location in the peer_ip map
	for hostname, host in peer_ip.peer_map.items():
		name = str(eval(hostname)[4][0][1])
		if(host_input == name):
			host_location = host
	if(host_location == None):
		print("Host not found")
		return
	print("Asking", host_input, "if she knows")

	return client_methods.send_question(peer_name, query, host_location)