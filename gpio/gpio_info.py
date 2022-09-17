import RPi.GPIO as GPIO

print(f'GPIO VERSION: {GPIO.VERSION}')
print('GPIO full info:')
print(GPIO.RPI_INFO)
print(f'REVISION: {GPIO.RPI_INFO["P1_REVISION"]}')
print(f'REVISION: {GPIO.RPI_REVISION}')
