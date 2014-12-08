import server_side_connection
import client_side_connection
import network_protocol
import peer_ip
import client_methods
import ast
import fileIO
from pyDatalog import pyDatalog

def answerQuestion(peer_name, net, user_password):
	policy_filename = 'entities/' + peer_name + '/datalog_policy.data'
	data_filename = 'entities/' + peer_name + '/data.data'

	queryString = net.recv();
	queryList = queryString.split(network_protocol.SEPARATOR)
	print(queryList)

	trusted_peer_dict = getTrustedPeers(peer_name)
	for other_peer, trusted_with in trusted_peer_dict.items():
		data = getDataFromTrustedPeer(peer_name, other_peer, user_password)
		pruned_data = prune(data, trusted_with)
		add_facts(pruned_data)

	# Add our own data
	if(fileIO.fileExists(data_filename)):
		add_facts(fileIO.readFile(data_filename))

	pyDatalog.load(fileIO.readFile(policy_filename))

	query_result = pyDatalog.ask(queryList[0]);
	print('Query result:',query_result)
	if(query_result != None):
		net.send(queryList[1])
	else:
		net.send(queryList[2])


def getDataFromTrustedPeer(peer_name, other_peer, user_password):
	# lookup the location of the other host
	host_location = peer_ip.getHostLocation(other_peer)

	# Connect to the appropriate host
	net = client_side_connection.ClientSideConnection(
		peer_name = peer_name, ip = host_location[0], portno = int(host_location[1]), password = user_password)

	net.send("Gimme_yo_data")

	data = net.recv()
	print('Got some data from',other_peer)
	return data

def getTrustedPeers(peer_name):
	trusted_peers_filename = 'entities/' + peer_name + '/trusted_peers.data'
	contents = fileIO.readFile(trusted_peers_filename)
	return ast.literal_eval(contents)

def sendData(peer_name, net):
	data_filename = 'entities/' + peer_name + '/data.data'

	print(net.getPeerInfo()[4][0][1], 'asked for data')
	if(fileIO.fileExists(data_filename)):
		net.send(fileIO.readFile(data_filename))
	else:
		print('I don\'t have a data file! Sending None instead.')
		net.send('None')

# dataSet: "(('name', 'value'), ...)"
# trusted_with: {'WPI': 'WPIStudent', ...}
# returns subset of dataSet that contains only trusted elements
def prune(dataSet, trusted_with):
    evaluated_data = ast.literal_eval(dataSet)
    pruned = "("
    for e in evaluated_data:
        if e[0] == trusted_with:
            pruned += "('{0}', '{1}'),".format(e[0], e[1])
    pruned += ")"
    return pruned

# "(('name', 'value'), ...)"
# return void
def add_facts(pruned_data):
    print('adding data:', pruned_data)
    evaluated_data = ast.literal_eval(pruned_data)
    for entry in evaluated_data:
        pyDatalog.assert_fact(entry[0], entry[1])