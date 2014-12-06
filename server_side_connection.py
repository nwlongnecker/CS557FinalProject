import secure_context
import network_protocol
import socket
import peer_ip

class ServerSideConnection(object):

	def __init__(self, peer_name, password):
		hostlocation = peer_ip.getHostLocation(peer_name)

		self.secure_socket = secure_context.createListeningServerSocket(
		 		peer_name, hostlocation[0], int(hostlocation[1]), password)

	# Accepts the next connection. Must be called before send or recv
	def nextConnection(self):
		(client_connection, address) = self.secure_socket.accept()
		self.client_connection = client_connection

	# Sends data to the current connection
	def send(self, message):
		network_protocol.send(self.client_connection, message)

	# Receives data from the current connection
	def recv(self):
		return network_protocol.recv(self.client_connection)

	def getPeerInfo(self):
		return self.client_connection.getpeercert()['subject']

	# Closes the current connection
	# Should be called before calling nextConnection again
	def done(self):
		self.client_connection.shutdown(socket.SHUT_RDWR)

