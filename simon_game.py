import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED

colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13

LED.setup(R_pin, G_pin, B_pin)

def blinkColors():
	n = random.randint(0, 3)
	#colors.append(colors[n])
	#color_string = ' '.join(colors)
	#for i in range(0, len(colors)):
		#print colors[i].lower()
		#time.sleep(1)
	LED.setColor(colors[n])
	time.sleep(0.5)
	LED.noColor()
	time.sleep(0.5)
	

if __name__ == '__main__':
	try:
		while True:
			blinkColors()
	except KeyboardInterrupt:
		LED.destroy()
		print ' See ya later, Alligator'












