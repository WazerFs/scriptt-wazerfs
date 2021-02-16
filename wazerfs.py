import os
from time import sleep
os.system('clear')
sleep(0.8)
print('\033[34m===\033[m'*18)
print('''\033[36m	WAZER FS 
\033[m
	[ 1 ] Dados
	[ 2 ] Web Ferramentas
	[ 3 ] Malwares
	[ 4 ] Wifi / Acesso point
	[ 5 ] Tools
	[ 6 ] Ferramentas
	[ 0 ] Finalizar''')
print('\033[34m===\033[m'*18)
frr = int(input('\n\033[35mEscolha uma opção: \033[m'))
if frr == 1:
	os.system('clear')
	print('\033[36m	DADOS\033[m')
	print('\033[34m=-=\033[m' * 10)
	print('''
	[ 1 ] ISQNetool
	[ 2 ] Sinespy
	[ 0 ] Menu/finalizar''')
	print('\033[34m=-=\033[m' * 10)
	n1 = int(input('\nOpção: '))
	if n1 == 1:
		   os.system('git clone https://github.com/Isqne/isqnetool')
	elif n1 == 2:
		os.system('git clone https://github.com/Luan-Devecchi/sinespy')
	sc = str(input('Voltar ao menu?(s/n): ')).strip()
	if sc == 'N' or sc == 'n':
		os.system('exit')
	elif sc == 'S' or sc == 's':
		os.system('python3 wazerfs.py')
	else:
		print('\nOPÇÃO INVÁLIDA')
		
		
		
elif frr == 2:
	os.system('clear')
	print('\033[36m	WEB FERRRAMENTAS\033[m')
	print('\033[34m=-=\033[m' * 10)
	print('''
	[ 1 ] XSStrike
	[ 2 ] ZomNet
	[ 3 ] 1NFO HUNT3R
	[ 4 ] Detetive-URL
	[ 5 ] Injected-framework
	[ 0 ] Menu/finalizar''')
	print('\033[34m=-=\033[m' * 10)
	n2 = int(input('\nOpção: '))
	if n2 == 1:
		os.system('git clone https://github.com/s0md3v/XSStrike')
	elif n2 == 2:
		os.system('git clone https://github.com/MrEmpy/ZomNet.git')
	elif n2 == 3:
		os.system('git clone https://github.com/MrEmpy/1nf0-hunt3r.git')
	elif n2 == 4:
		os.system('git clone https://github.com/MrEmpy/Detective-URL')
	elif n2 == 5:
		os.system('git clone https://github.com/Cesar-Hack-Gray/Injected-framework ')
		
		
	sc = str(input('Voltar ao menu?(s/n): ')).strip()
	if sc == 'N' or sc == 'n':
		os.system('exit')
	elif sc == 'S' or sc == 's':
		os.system('python3 wazerfs.py')
	else:
		print('\nOPÇÃO INVALIDA')
		
		
		
elif frr == 3:
	os.system('clear')
	print('\033[36m	MALWARES\033[m')
	print('\033[34m=-=\033[m' * 10)
	print('''
	[ 1 ] Malicious
	[ 2 ] RansoWare
	[ 0 ] Menu/finalizar ''')
	print('\033[34m=-=\033[m' * 10)
	n3 = int(input('Opção: '))
	if n3 == 1:
		os.system('git clone https://github.com/TheReaper167/Malicious')
	elif n3 == 2:
		os.system('git clone https://github.com/bug7sec/Ransomware')
	sc = str(input('Voltar ao menu?(s/n): ')).strip()
	if sc == 'N' or sc == 'n':
		os.system('exit')
	elif sc == 'S' or sc == 's':
		os.system('python3 wazerfs.py')
	else:
		print('\nOPÇÃO INVÁLIDA')
		
		
		
elif frr == 4:
	os.system('clear')
	print('\033[36m	WIFI\033[m')
	print('\033[34m=-=\033[m' * 10)
	print('''
	[ 1 ] WifiPhiser
	[ 2 ] Wifi-Cracking
	[ 3 ] Wifi Jammer
	[ 4 ] Wifi Pumpiking3 
	[ 5 ] Routersploit
	[ 0 ] Menu/finalizar''')
	opc = int(input('Opção: '))
	if opc == 1:
		os.system('git clone https://github.com/wifiphisher/wifiphisher')
	elif opc == 2:
		os.system('git clone https://github.com/brannondorsey/wifi-cracking')
	elif opc == 3:
		os.system('git clone https://github.com/DanMcInerney/wifijammer')
	elif opc == 4:
		os.system('git clone https://github.com/P0cL4bs/wifipumpkin3')
	elif opc == 5:
		os.system('git clone https://www.github.com/threat9/routersploit')
	sc = str(input('Voltar ao menu?(s/n): ')).strip()
	if sc == 'N' or sc == 'n':
		os.system('exit')
	elif sc == 'S' or sc == 's':
		os.system('python3 wazerfs.py')
	else:
		print('\nOPÇÃO INVÁLIDA')
		
		
		
elif frr == 5:
	os.system('clear')
	print('\033[36m	TOOLS\033[m')
	print('\033[34m=-=\033[m' * 10)
	print(''' 
	[ 1 ] HCXTools
	[ 2 ] LordPhish
	[ 3 ] SocialSploit
	[ 4 ] Lazymux
	[ 5 ] Fsociety
	[ 0 ] Menu/finalizar ''')
	print('\033[34m=-=\033[m' * 10)
	n5 = int(input('Opção: '))
	if n5 == 1:
		os.system('git clone https://github.com/ZerBea/hcxtools')
	elif n5 == 2:
		os.system('git clone https://github.com/grenoxx/LordPhish.git')
	elif n5 == 3:
		os.system('git clone https://github.com/Cesar-Hack-Gray/SocialSploit')
	elif n5 == 4:
		os.system('git clone https://github.com/Gameye98/Lazymux')
	elif n5 == 5:
		os.system('git clone https://github.com/Manisso/fsociety')
	sc = str(input('Voltar ao menu?(s/n): ')).strip()
	if sc == 'N' or sc == 'n':
		os.system('exit')
	elif sc == 'S' or sc == 's':
		os.system('python3 wazerfs.py')
	else:
		print('\nOPÇÃO INVÁLIDA')
		
		
		
elif frr == 6:
	os.system('clear')
	print('\033[36m	TERMUX-FERRAMENTAS\033[m')
	print('\033[34m=-=\033[m' * 10)
	print(''' 
	[ 1 ] Ngrok
	[ 2 ] Sqlmap
	[ 3 ] Metasploit
	[ 4 ] Tstyling
	[ 5 ] Black Hydra
	[ 0 ] Menu/finalizar ''')
	print('\033[34m=-=\033[m' * 10)
	n6 = int(input('Opção: '))
	if n6 == 1:
		os.system('git clone https://github.com/inconshreveable/ngrok')
	elif n6 == 2:
		os.system('git clone https://github.com/sqlmapproject/sqlmap')
	elif n6 == 3:
		os.system('git clone https://github.com/rapid7/metasploit-framework')
	elif n6 == 4:
		os.system('git clone https://github.com/darkwarrior3/tstyling')
	elif n6 == 5:
		os.system('git clone https://github.com/Gameye98/Black-Hydra')
	sc = str(input('Voltar ao menu?(s/n): ')).strip()
	if sc == 'N' or sc == 'n':
		os.system('exit')
	elif sc == 'S' or sc == 's':
		os.system('python3 wazerfs.py')
	else:
		print('\nOPÇÃO INVÁLIDA')
		
		
		
elif frr == 0:
	os.system('clear')
	dj = str(input('Deseja finalisar? (s/n): ')).upper()
	if dj == 'S':
		os.system('exit')
	elif dj == 'N':
		print('Vamos voltar então...')
		sleep(1.2)
		os.system('python3 wazerfs.py')
		