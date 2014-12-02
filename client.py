import parse_params
import client_side_connection
import re
import sys
import client_methods

peer_name = parse_params.getUsername(server_side = False)

print('Hello ', peer_name)

while True:
	print()
	print('What would you like to do?')
	print('1. Ask Question')
	print('2. Exit')

	accepted = False
	while not accepted:
		# Running this on python3; input does not evaluate data
		value = input('1-2: ')
		if re.match('\A[1-2]\Z', value):
			accepted = True

	if(value == '1'):
		print()
		client_methods.ask_question(peer_name);
	elif(value == '2'):
		print('Goodbye', peer_name)
		sys.exit()
