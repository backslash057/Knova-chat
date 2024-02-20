import mysql.connector


database = ""
conn = None

def init(host, user, pwd, database):
	global conn, dbname

	dbname = database
	
	conn = mysql.connector.connect(
		host=host,
		user=user,
		password=pwd
	)

	cursor = conn.cursor()

	cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbname} DEFAULT CHARACTER SET 'utf8'")
	cursor.execute(f"USE {dbname}")

	clear_database()
	init_tables()



def clear_database():
	global conn
	cursor = conn.cursor()

	cursor.execute("SHOW TABLES FROM {}".format(dbname))

	for table in cursor.fetchall():
		query = f"DROP TABLE {table[0]};"
		cursor.execute(query)
	conn.commit()
	cursor.close()


def init_tables():
	global conn
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS users (
			id varchar(30) PRIMARY KEY,
			username varchar(30) NOT NULL, 
			password varchar(100) NOT NULL,
			lastinteraction TIMESTAMP NOT NULL
		)
		"""
	)

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS chats (
			chatId varchar(30) PRIMARY KEY,
			user1 varchar(30) NOT NULL,
			user2 varchar(30) NOT NULL
		)
		"""
	)

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS messages (
			messageId INTEGER PRIMARY KEY AUTO_INCREMENT,
			send_time timestamp NOT NULL,
			content text NOT NULL,
			status enum('sent','received','read') NOT NULL,
			senderId varchar(30) DEFAULT NULL,
			receiverId varchar(30) DEFAULT NULL,
			chatId varchar(30) DEFAULT NULL
		)
		"""
	)

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS user_chat (
			userChatd varchar(30) PRIMARY KEY,
			userId varchar(30) DEFAULT NULL,
			chatId varchar(30) DEFAULT NULL
		)
		"""
	)

	conn.commit()
	cursor.close()


def user_exists(userid):
	global conn
	cursor = conn.cursor()

	query = "SELECT * FROM users WHERE id=%s"

	cursor.execute(query, (userid,))
	result = cursor.fetchone()

	cursor.close()
	return result != None

def register(userid, username, password):
	global conn
	cursor = conn.cursor()

	query = "INSERT INTO users VALUES (%s, %s, %s, %s)"

	#chiffrement du mot de passe avant enregistrement

	cursor.execute(query, (userid, username, password, None))
	conn.commit()
	cursor.close()


def check_user(userid, password) -> str:
	global conn

	cursor = conn.cursor()

	query = "SELECT username FROM users WHERE id=%s AND password=%s"

	# chiffrement du mot de passe avant verification

	cursor.execute(query, (userid, password))
	username = cursor.fetchone()

	cursor.close()
	return username[0]
