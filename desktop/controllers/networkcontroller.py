import socket
import json
import time

from models.exeptions import AuthException

class Network():
	def init(self, netconf):
		try:
			self.host = netconf['host']
			self.port = netconf['port']

			self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except KeyError:
			print("Could not parse network config file. The app could not connect to server :(")
			self.conn = None

		

	def connect(self):
		if not self.conn: return

		try:
			self.conn.connect((self.host, self.port))
		except (ConnectionAbortedError, ConnectionRefusedError, ) as e:
			print(f"Connection to {self.host}:{self.port} failed, Reconnecting...")
			time.sleep(0.5)
			self.connect()	

		print("Network connected")
		self.receive()


	def send(self, datas):
		self.conn.send(datas.encode("utf8"))


	def receive(self):
		try:
			while True:
				byte = self.conn.recv(1024)

				if not byte: break

				paquet = byte.decode("utf8")
				data = json.loads(paquet)

				print(data)

				if data['type'] == "REG_SUCCES":
					user.current = user.User(
						userid=data['body']['id'],
						username = data['body']['user']
					)

		except ConnectionError as e:
			print("Network disconnected")
			self.connect()


def send_auth_datas(username, nickname, password):
	datas = {}
	datas["body"] = {
		"id": username,
		"pwd": password
	}

	if nickname:
		datas["type"] = "REGISTER"
		datas["body"]["user"] = nickname
	else: datas["type"] = "LOGIN"
	
	print(datas)
	packet = json.dumps(datas)
	network.send(packet)


network = Network()
