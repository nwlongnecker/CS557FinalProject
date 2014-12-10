import client_side_connection
import peer_ip
import network_protocol
import random
	
def ask_question(peer_name):

	host_input = 'InviteTracker'
	host_location = peer_ip.getHostLocation(host_input)

	student_name = input('Student\'s name (Ryan, Joey, Goliath, ...): ')
	student_school = input('Student\'s school (WPI, HolyCross, Clark): ')
	student_club = input('Student\'s club (ACM, UPE): ')

	#Question string should not have any network_protocol.SEPARATOR in it. (No semicolons)
	question = 'invited(' + student_name + ',' + student_school + ',' + student_club + ')'
	print('Asking:', question)

	answer = send_question(peer_name, question, host_location)
	# print the response
	if(answer):
		print(question, '->', 'Yes')
	else:
		print(question, '->', 'No')

def send_question(peer_name, question, host_location):

	yesNum = str(random.random())
	noNum = str(random.random())

	# Connect to the appropriate host
	net = client_side_connection.ClientSideConnection(
		peer_name = peer_name, ip = host_location[0], portno = int(host_location[1]))

	net.send('Query')
	queryString = question + network_protocol.SEPARATOR + yesNum + network_protocol.SEPARATOR + noNum
	net.send(queryString)

	answer = net.recv()
	net.done()

	if(answer == yesNum):
		return True
	elif(answer == noNum):
		return False
	else:
		print("Something went wrong")
		return False
