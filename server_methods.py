import server_side_connection
import network_protocol
import random

def answerQuestion(peer_name, net):
	queryString = net.recv();
	queryList = queryString.split(network_protocol.SEPARATOR)
	print(queryList)

	# If the answer is yes, send the yes number, otherwise send the no number
	if(solve(queryList[0])):
		net.send(queryList[1])
	else:
		net.send(queryList[2])

def solve(query):
	answer = random.random() > 0.5
	print("Random answer:", answer)
	return answer