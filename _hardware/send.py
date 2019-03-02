import requests
ADDR = "http://127.0.0.1:8000/library_monitor/"

def update(op, room):
	# Make a get request to get the latest position of the international space station from the opennotify api.
	if op == 'enter':
		response = requests.get(ADDR+room+"/enter")
		# Print the status code of the response.
		print(response.text)
	elif op == 'leave':
		response = requests.get(ADDR+room+"/enter")
		print(response.text)
	elif op == 'check':
		response = requests.get(ADDR+room)
		print(response.text)
	else:
		print('Invalid Input')


print('Available Input: [enter/leave/check] [room number/floor number]')

while True:
	uin = input('-------\n')
	oplist = uin.split(' ')
	# print(oplist)
	if len(uin)==0:
		break
	else:
		update(oplist[0],oplist[1])
