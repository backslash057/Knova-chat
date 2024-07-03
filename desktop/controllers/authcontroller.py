from string import ascii_letters, ascii_lowercase, digits


def validate_username(username):
	chars = set(ascii_lowercase + digits + '_')
	letters = set(username)

	if len(username) == 0:
		return "User id required"

	if not all([letter in chars  for letter in letters]):
		return "User id is lowercase letters and digits only."


def validate_nickname(nickname):
	chars = set(ascii_letters + digits + '_')
	letters = set(nickname)

	if len(nickname) == 0:
		return "Nickname required."

	if len(nickname) < 4:
		return "Too short nickname."

	if not all([letter in chars for letter in letters]):
		return "Nickname is letters and digits only."



def validate_password(password):
	if password == '':
		return "Password required."

	if len(password) < 8:
		return "Invalid password."