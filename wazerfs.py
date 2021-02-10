from time import sleep
print('\033[34m___\033[m'*20)
print('''\033[36mWazer Ferramentas:\033[m
	[ 1 ] Puxar dados
	[ 2 ] DDos
	[ 3 ] Vírus
	[ 4 ] Wifi / Acesso point
	[ 5 ] Tools
	[ 6 ] WebCam''')
print('\033[34m___\033[m'*20)
frr = int(input('\033[35mEscolha uma opção: \033[m'))
if frr == 1:
	print('''
	[1] ISQNetool
	[2] Sinespy
	[0] Menu/finalizar''')
	n1 = int(input('Opção: '))
	if n1 == 1:
		   print('\033[31mReforma\033[m')
	elif n1 ==2:
				print('\033[31Reforma\033[m')
	else:
		print('\nOPÇÃO INVÁLIDA')
elif frr == 2:
	print('''
	[1] Sql Injection
	[0] Menu/finalizar''')
	n2 = int(input('Opção: '))
	if n2 == 1:
		print('\033[31mReforma\033[m')
	else:
		print('\nOPÇÃO INVÁLIDA')
elif frr == 3:
	print('''
	[1] Malicious
	[2] RansoWare
	[0] Menu/finalizar ''')
	n3 = int(input('Opção: '))
	if n3 == 1:
		print('\033[31mReforma\033[m')
	elif n3 == 2:
		print('\033[31mReforma\033[m')
	else:
		print('\nOPÇÃO INVÁLIDA')
elif frr == 4:
	print('''
	[1] WifiPhiser
	[2] Wifi-Cracking
	[3] Wifi Jammer
	[4] Wifi Pumpiking3 
	[0] Menu/finalizar''')
	n4 = int(input('Opção: '))
	if n4 == 1:
		print('\033[31mReforma\033[m')
	elif n4 == 2 or n4 == 3 or n4 == 4:
		print('\033[31mReforma\033[m')
	else:
		print('\nOPÇÃO INVÁLIDA')
elif frr == 5:
	print(''' 
	[1] HCXTools
	[0] Menu/finalizar ''')
	n5 = int(input('Opção: '))
	if n5 == 1:
		print('\033[31mReforma\033[m')
	else:
		print('\nOPÇÃO INVÁLIDA')
elif frr == 6:
	print(''' 
	[1] WebCam
	[0] Menu/finalizar ''')
	n6 = int(input('Opção: '))
	if n6 == 1:
		print('\033[31mReforma\033[m')
	else:
		print('\nOPÇÃO INVÁLIDA')
	