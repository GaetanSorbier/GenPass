import random 
from colorama import *

init()

print(Fore.BLUE + """  ________                 __________                         
 /  _____/   ____    ____  \______   \_____     ______  ______
/   \  ___ _/ __ \  /    \  |     ___/\__  \   /  ___/ /  ___/
\     \_\  \\  ___/ |   |  \ |    |     / __ \_ \___ \  \___ \ 
 \______  / \___  >|___|  / |____|    (____  //____  >/____  >
        \/      \/      \/                 \/      \/      \/ 
                                            By Gaetan Sorbier\n""")

print(Fore.GREEN + "1 - Mot de passe normal : 8 caractères , contenant lettres majuscules et minuscules avec chiffres\n2 - Mot de passe sécurisé : Plus de 8 caractères contenant lettres majuscules et minuscules , avec chiffres et caractères spéciaux\n3 - Mot de passe Ultra Pro Max : Le mot de passe du chef !\n4 - Mot de passe personalisable : Choisissez le nombre de caractères que contiendra votre mot de passe\n")
level = input("Choisissez une option : ")
def npass():
	chars = "abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

	password = ''

	for i in range(8):
		password = f"{password}{random.choice(chars)}"		

	print(f"Mot de passe : {password}")

	with open("password.txt", "a+") as file:
		file.write(f"Mot de passe : {password}\n")
		file.close()

	print("\nVotre mot de passe est stocké dans le fichier password.txt")

def spass():
		chars = "abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,?;.:/!§%#@"

		password = ''

		for i in range(16):
			password = f"{password}{random.choice(chars)}"		

		print(f"Mot de passe : {password}")

		with open("password.txt", "a+") as file:
			file.write(f"Mot de passe : {password}\n")
			file.close()

		print("\nVotre mot de passe est stocké dans le fichier password.txt")
		
def hpass():
	chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.?!';:*%\/()+-&_€#@£¥$¢^={}×÷~[]<>"
	
	password = ''
	
	for i in range(32):
		password = f"{password}{random.choice(chars)}"
		
	print(f"Mot de passe : {password}")
	
	with open("password.txt", "a+") as file:
		file.write(f"Mot de passe : {password}\n")
		file.close()
	
	print("\nVotre mot de passe est stocké dans le fichier password.txt")
	
	
def cpass():
	choice = int(input("Choisissez le nombre de caractères que contiendra votre mot de passe : "))
	
	chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.?!';:*%\/()+-&_€#@£¥$¢^={}~[]<>"
	
	password = ''
	
	for i in range(choice):
		password = f"{password}{random.choice(chars)}"
		
	print(f"Mot de passe : {password}")
		
	with open("password.txt", "a+") as file:
		file.write(f"Mot de passe : {password}\n")
		file.close()
			
	print("\nVotre mot de passe est stocké dans le fichier password.txt")
	

if level == '1':
	npass()

if level == '2':
	spass()

if level == '3':
	hpass()

if level == '4':
	cpass()
