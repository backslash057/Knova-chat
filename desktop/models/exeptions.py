from dataclasses import dataclass

@dataclass
class AuthException(Exception):
	message: str

