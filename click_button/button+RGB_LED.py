import time
import sys
import traceback
import RPi.GPIO as GPIO


def pressButton():
    global cur_LED
    statusPinBtn = GPIO.input(pinBtn)
    # print(statusPinBtn)
    if statusPinBtn == 1:
        print('Button presed')
        if cur_LED == 0:
            GPIO.output(pinsLED[cur_LED], GPIO.HIGH)
            cur_LED = cur_LED + 1
        elif cur_LED == 1:
            GPIO.output(pinsLED[cur_LED], GPIO.HIGH)
            cur_LED = cur_LED + 1
        elif cur_LED == 2:
            GPIO.output(pinsLED[cur_LED], GPIO.HIGH)
            cur_LED = 0
        else:
            GPIO.output(pinsLED, GPIO.LOW)
        time.sleep(0.5)


def main():
    try:
        # якщо потрібно постійно виконувати код до преривання программи через Ctrl+C
        while True:
            pressButton()
    except KeyboardInterrupt:
        # ...
        print("Exit pressed Ctrl+C")
    except Exception:
        # ...
        print("Other Exception")
        print("--- Start Exception Data:")
        traceback.print_exc(limit=2, file=sys.stdout)
        print("--- End Exception Data:")
    finally:
        # ...
        print("CleanUp")
        GPIO.cleanup()
        print("End of program")


if __name__ == '__main__':
    pinBtn = 24
    pinsLED = [19, 13, 6]
    cur_LED = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinBtn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(pinsLED, GPIO.OUT, initial=0)
    main()
