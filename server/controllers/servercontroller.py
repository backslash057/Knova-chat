from socketserver import ThreadingMixIn, TCPServer

class ThreadedTCPServer(ThreadingMixIn, TCPServer):
	pass