import threading
import json

from views import logger

from models import dbmanager

from utils.constants import *

clients = {}


class Clienthandler(threading.Thread):
    def __init__(self, conn, addr):
        global clients
        threading.Thread.__init__(self)

        self.clients = clients
        self.conn = conn
        self.addr = addr


    def run(self):
        global clients
        logger.write(f"{self.addr} s'est connecté", logtype="DEBUG")

        while True:
            try:
                data = self.conn.recv(1024)
                if not data:
                    break

                data = json.loads(data.decode("utf8"))
                print(data)
                
                if data["type"] == "auth":
                    userid = data['id']
                    password = data['pwd']
                    response = self.authentify(userid, password)          

                self.conn.send(response.encode("utf8"))

            except Exception as e:
                print(e)

        clients.remove(self.conn)
        logger.write(f"{self.addr} s'est deconnecté", logtype=INFO)

    def authentify(self, userid, password):
        if not dbmanager.user_exists(userid):
            dbmanager.saveuser(userid, password)
            logger.write(f"User {userid} created", logtype=INFO)

            self.send_message(type=REQUEST, object="nickname", args=[])
        else:
            # recuperation des discussions avec des messages
            pass


    def send_message(self, **kwargs):
        self.conn.send(json.dumps(kwargs).encode("utf8"))
