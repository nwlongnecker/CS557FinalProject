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

	for other_peer, trusted_with in getTrustedPeers():
		data = getDataFromTrustedPeer(peer_name, peer)
		pruned_data = prune(data, trusted_with)
		add_facts(pruned_data)

	# Figure out what to do here later
	pyDatalog.ask(queryList[0])

	net.send(queryList[1])

def getDataFromTrustedPeer(peer_name):
	return "data"

def getTrustedPeers():
	return {('a', 'a')}

# Marc dictates format
# String: "[('predicate', 'arg1', 'arg2', ...), ('predicate', args), ...]""
# return whatever argument you want for add_facts
def prune(dataSet, trusted_with):
	return dataSet

# [('predicate', args...), ('predicate', args), ...]
# return void
def add_facts(pruned_data):
	print(pruned_data)
	#pyDatalog.assert_fact('parent', 'bill', 'John Adams')