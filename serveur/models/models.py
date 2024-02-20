
class Message:
	def __init__(self, messageId, senderId, chatId, content, status, sendtime):
		self.essageId = messageId
		self.senderId = senderid
		self.chatId = chatId
		self.content = content
		self.status = status
		self.sendtime = sendTime

class User():
	def __init__(self, id_, nickname, lastinteraction=None):
		self.id = userid
		self.nickname = nickname
		self.lastinteraction = lastinteraction


class chat:
	def __init__(self, chatId, chatname=None):
		self.chatId = chatId
		self.chatName = chatname