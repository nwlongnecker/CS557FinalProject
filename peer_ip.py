import ast
import sys

# This map uses the peer subject section of their certificate as a key
# when looking up their IP and portnumber.
# This file could either be redistributed to all clients each time someone's
# ip changes or someone is added to the network, or it could be replaced by a
# broadcast system for finding other peers willing to host
peer_map = {
	"((('countryName', 'US'),), (('stateOrProvinceName', 'Massachusetts'),), (('organizationName', 'cs557'),), (('organizationName', 'Nathan Longnecker'),), (('commonName', 'Clark'),))":
	('127.0.0.1', '5571'),
	"((('countryName', 'US'),), (('stateOrProvinceName', 'Massachusetts'),), (('organizationName', 'cs557'),), (('organizationName', 'Nathan Longnecker'),), (('commonName', 'ClarkACM'),))":
	('127.0.0.1', '5572'),
	"((('countryName', 'US'),), (('stateOrProvinceName', 'Massachusetts'),), (('organizationName', 'cs557'),), (('organizationName', 'Nathan Longnecker'),), (('commonName', 'ClarkUPE'),))":
	('127.0.0.1', '5573'),
	"((('countryName', 'US'),), (('stateOrProvinceName', 'Massachusetts'),), (('organizationName', 'cs557'),), (('organizationName', 'Nathan Longnecker'),), (('commonName', 'HolyCross'),))":
	('127.0.0.1', '5574'),
	"((('countryName', 'US'),), (('stateOrProvinceName', 'Massachusetts'),), (('organizationName', 'cs557'),), (('organizationName', 'Nathan Longnecker'),), (('commonName', 'HolyCrossACM'),))":
	('127.0.0.1', '5575'),
	"((('countryName', 'US'),), (('stateOrProvinceName', 'Massachusetts'),), (('organizationName', 'cs557'),), (('organizationName', 'Nathan Longnecker'),), (('commonName', 'HolyCrossUPE'),))":
	('127.0.0.1', '5576'),
	"((('countryName', 'US'),), (('stateOrProvinceName', 'Massachusetts'),), (('organizationName', 'cs557'),), (('organizationName', 'Nathan Longnecker'),), (('commonName', 'WPI'),))":
	('127.0.0.1', '5577'),
	"((('countryName', 'US'),), (('stateOrProvinceName', 'Massachusetts'),), (('organizationName', 'cs557'),), (('organizationName', 'Nathan Longnecker'),), (('commonName', 'WPIACM'),))":
	('127.0.0.1', '5578'),
	"((('countryName', 'US'),), (('stateOrProvinceName', 'Massachusetts'),), (('organizationName', 'cs557'),), (('organizationName', 'Nathan Longnecker'),), (('commonName', 'WPIUPE'),))":
	('127.0.0.1', '5579'),
	"((('countryName', 'US'),), (('stateOrProvinceName', 'Massachusetts'),), (('organizationName', 'cs557'),), (('organizationName', 'Nathan Longnecker'),), (('commonName', 'InviteTracker'),))":
	('127.0.0.1', '5580')
}

def getHostLocation(host_input):
	host_location = None
	# Look up the host location in the peer_ip map
	for hostname, host in peer_map.items():
		name = str(ast.literal_eval(hostname)[4][0][1])
		if(host_input == name):
			host_location = host
	if(host_location == None):
		print("Host not found:", host_input)
		sys.exit()

	return host_location