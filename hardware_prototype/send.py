# http://www.flom.ml/332B/enter/aaaaaa
import requests
import sys
ADDR = "http://www.flom.ml/"

def update(op, room, secret):
	if op == 'enter':
		# Make a get request to get the latest position of the international space station from the opennotify api.
		response = requests.get(ADDR+str(room)+"/enter"+secret)
		# Print the status code of the response.
		print(response.text)
	elif op == 'leave':
		response = requests.get(ADDR+str(room)+"/leave"+secret)
		print(response.text)
	# elif op == 'check':
	# 	response = requests.get(ADDR+str(room))
	# 	print(response.text)
	else:
		print('Invalid Input')

if sys.argv[1]=='test':
	print('Available Input: [enter/leave] [room number/floor number] [secret key]')
	while True:
		uin = input('-------\n')
		oplist = uin.split(' ')
		# print(oplist)
		if len(uin)==0:
			break
		else:
			update(oplist[0],oplist[1])
