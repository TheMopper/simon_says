import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin, 1000)

colors = ['R', 'G', 'B', 'Y']
colorList = []
guessedColors = []

frequencies = [220, 440, 880, 1760]
R_pin = 11
G_pin = 12
B_pin = 13

turn = 1

LED.setup(R_pin, G_pin, B_pin)

def blinkColors():
	n = random.randint(0, 3)
	#colors.append(colors[n])
	#color_string = ' '.join(colors)
	#for i in range(0, len(colors)):
		#print colors[i].lower()
		#time.sleep(1)
	colorList.append(colors[n])

	
	Buzz.ChangeFrequency(frequencies[n])
	Buzz.start(50)
	
	print colors[n]

	LED.setColor(colors[n])
	time.sleep(0.5)
	Buzz.stop()

	LED.noColor()
	time.sleep(0.5)

def playColorList():
	for i in range(0, len(colorList)):
		Buzz.ChangeFrequency(220 * (2 ** colors.index(colorList[i])))
		Buzz.start(50)
		LED.setColor(colorList[i])
		time.sleep(0.5)
		Buzz.stop()
		LED.noColor()
		time.sleep(0.5)

def addNewColor():
	n = random.randint(0, 3)
	colorList.append(colors[n])

def guessColors():
	guessNumber = 0
	guessedColor = raw_Input()
	if guessedColor == 'r' or guessedColor == 'g' or guessedColor == 'b' or guessedColor == 'y':
		guessedColors.append(guessedColor)

		if guessedColors[guessNumber] != colorList[Number]:
			print "GAME OVER!"
		
	else:
		print "Invalid input, please try again"


if __name__ == '__main__':
	try:
		while True:
			addNewColor()
			playColorList()
			time.sleep(1.5)
	except KeyboardInterrupt:
		LED.destroy()
		print ' See ya later, Alligator'


























