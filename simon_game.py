import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Buzzer stuff
buzz_pin = 32
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin, 1000)
frequencies = [220, 440, 880, 1760]

colors = ['R', 'G', 'B', 'Y']
colorList = []
gameOver = False

#LED stuff
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)



def addNewColor():
	n = random.randint(0, 3)
	colorList.append(colors[n])

def playColorList():
	for i in range(0, len(colorList)):
		Buzz.ChangeFrequency(220 * (2 ** colors.index(colorList[i])))
		Buzz.start(50)
		LED.setColor(colorList[i])
		#print colorList[i]
		time.sleep(0.5)
		Buzz.stop()
		LED.noColor()
		time.sleep(0.5)
	print ' '

def guessColors():
	print "Start Guessing!"
	Buzz.ChangeFrequency(300)
	Buzz.start(50)
	time.sleep(0.2)
	Buzz.stop()
	
	guessString = raw_input()
	if list(guessString.upper()) == colorList:
		print "Correct"
		return True
	else:
		print "Oh No!"
		return False
	

if __name__ == '__main__':
	try:
		addNewColor()
		playColorList()
		while guessColors():
			addNewColor()
			playColorList()
			time.sleep(1.5)
		print "You Lost!"
	except KeyboardInterrupt:
		LED.destroy()
		print ' See ya later, Alligator'

