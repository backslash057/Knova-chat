import os.path
import socket
import sys
from configparser import ConfigParser
from views.logger import logtypes
from views import logger
from controllers.servercontroller import ThreadedTCPServer
from controllers import clientcontroller
from models import dbmanager
from utils.constants import *


#initializing the logger
logpath = os.path.join(os.path.dirname(__file__), "logs")
logger.init(logpath, sym=">> ")


configpath = os.path.join(os.path.dirname(__file__), "config.ini")
parser = ConfigParser()
parser.read(configpath)

host=parser.get("mysql", "host")
user=parser.get("mysql", "user")
pwd=parser.get("mysql", "password")
dbname=parser.get("mysql", "dbname")

logger.write("Connecting to MySQL database", logtype=logtypes.INFO)
try:
	dbmanager.init(host, user, pwd, dbname)
except Exception as e:
	logger.write("Connection to database failed", logtype=logtypes.ERROR)
	sys.exit(1)
else:
	logger.write("MySQL database connected")

nethost = parser.get("connexion", "host")
netport = int(parser.get("connexion", "port"))

logger.write("Starting server...", logtype=logtypes.INFO)
try:
	server = ThreadedTCPServer((nethost, netport), clientcontroller.ClientHandler)
	logger.write(f"Server started at port {netport}", logtype=logtypes.INFO)
except:
	logger.write("Server start failed. Maybe the selected port is already in use", logtype=logtypes.ERROR)
	sys.exit(1)

try:
	server.serve_forever()
except KeyboardInterrupt:
	logger.write("Stopping server", logtype=logtypes.INFO)
	for connection in clientcontroller.clients:
		connection.close()
	server.shutdown()
	server.server_close()
