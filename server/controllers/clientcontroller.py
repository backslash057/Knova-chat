from socketserver import BaseRequestHandler

from views import logger

from models import dbmanager

import json

clients = {}

class ClientHandler(BaseRequestHandler):
	def handle(self):
		logger.write(f"{self.client_address} connected")

		try:
			while True:
				byte = self.request.recv(1024)
				paquet = byte.decode("utf8")
				data = json.loads(paquet)

				clients[self.request] = {"address": self.client_address}

				if not data: break

				if data['type'] == "REGISTER":
					response = register(data['body'])
					paquet = json.dumps(response)
					self.request.send(paquet.encode("utf8"))
				if data['type'] == "LOGIN":
					response = login(data['body'])
					paquet = json.dumps(response)
					self.request.send(paquet.encode("utf8"))
					
				print(data)
		except (ConnectionResetError, ConnectionAbortedError):
			pass


	def finish(self):
		#clients.pop()
		logger.write(f"{self.client_address} disconnected")


def register(data):
	userid = data['id']
	username = data['user']
	password = data['pwd']

	if dbmanager.user_exists(userid):
		return {"type": "REG_ERROR", "body":{"message": f"User {userid} already exists."}}

	dbmanager.register(userid, username, password)
	return {"type": "REG_SUCCES", "body": {"id": "userid", "user": username}}


def login(data):
	userid = data['id']
	password = data['pwd']

	username = dbmanager.check_user(userid, password)

	if not username:
		return {"type": "LOGIN_ERR", "body": {"message": f"Incorrect userId or password"}}
	
	return {"type": "LOGIN_SUCCES", "body": {"id": userid, "user": username}}
