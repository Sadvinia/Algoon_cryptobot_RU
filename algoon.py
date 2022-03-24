import os
import time
while True:
	def banner():
		os.system("cls")
		print("""        _                         
   /\  | |                        
  /  \ | | ____  ___   ___  ____  
 / /\ \| |/ _  |/ _ \ / _ \|  _ \ 
| |__| | ( ( | | |_| | |_| | | | |
|______|_|\_|| |\___/ \___/|_| |_|
         (_____|                  """)
		print("")
	def dialog():
		print('1.Продолжить 2.Выйти')
		answer = input(">>> ")
		if answer == '1':
			pass
		elif answer == '2':
			banner()
			time.sleep(1)
			exit()
		else:
			print('Неверная операция!')
	banner()
	print("Вас приветствует криптобот Algoon\nMade by Lutay INC.\nVersion 0.7\nРусский язык ONLY!")
	print("""Выбирете режим работы:
	1.Шифровать
	2.Расшифровать
	3.Выход""")
	answer = input(">>> ")
	if answer == '1':
		print("Введите сообщение:")
		passwd = input(">>> ")
		passwd0 = passwd.lower()
		print("Идёт обработка, подождите...")
		def parsing(target, replacevalues):
			for i, j in replacevalues.items():
				target = target.replace(i, j)
				print(target)
			print('Ваше сообщение >>> ' + target)
		rpvalues = {'а': 'ÿ','б': '%','в': 'P','г': '*','д': '=','е': '№','ё': '~','ж': '<','з': '^','и': '$','й': '+','к': '-','л': '/','м': '7','н': ']','о': '9','п': 'Ô','р': 'Ð','с': 'þ','т': 'Œ','у': 'Q','ф': '(','х': 'z','ц': '&','ч': '@','ш': 'Š','щ': 'ƒ','ъ': 'ž','ы': '©','ь': 'Â','э': 'N','ю': '¿','я': '»'}
		passwd1 = parsing(passwd0,rpvalues)
		dialog()
	elif answer == '2':
		print("Введите полученное сообщение:")
		quest = input(">>> ")
		print("Идёт обработка, подождите...")
		def question(target, replaceval):
			for i, j in replaceval.items():
				target = target.replace(i, j)
				print(target)
			print('Ваше сообщение >>> ' + target)
		rpval = {'»' :'я','¿' :'ю','N' :'э','Â' :'ь','©' :'ы','ž' :'ъ','ƒ' :'щ','Š' :'ш','@' :'ч','&' :'ц','z' :'х','(' :'ф','Q' :'у','Œ' :'т','þ' :'с','Ð' :'р','Ô' :'п','9' :'о',']' :'н','7' :'м','/' :'л','-' :'к','+' :'й','$' :'и','^' :'з','<' :'ж','~' :'ё','№' :'е','=' :'д','*' :'г','P' :'в','%' :'б','ÿ' :'а'}
		quest1 = question(quest,rpval)
		dialog()
	elif answer == '3':
		banner()
		time.sleep(1)
		exit()
	else:
		print("Неверная операция!")
