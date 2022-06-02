from time import sleep
from random import choice

while True:
	text = ''
	for i in range(choice(range(4, 68))):
		text += choice(['z', 'Z'])	
	print(text)
	sleep(2)