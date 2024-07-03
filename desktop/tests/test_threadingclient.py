import threading
import threading
import time
import sys

def thread_message():
    time.sleep(3)  # Attente de 3 secondes (simule un message venant du thread)
    print("\033[F")  # Déplace le curseur vers le haut d'une ligne
    print("Message du thread : Hello, world!\nMessage: ", end="")

# Démarrer le thread pour afficher le message
threading.Thread(target=thread_message).start()

# Boucle d'entrée principale
while True:
    user_input = input("Message: ")
    print(user_input)