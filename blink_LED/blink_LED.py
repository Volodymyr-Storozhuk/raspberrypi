import RPi.GPIO as GPIO
import time
import sys
import traceback


def main():
    try:
        # ініціалізація пінів
        LED_pin_Red = 19
        LED_pin_Green = 13
        LED_pin_Blue = 6
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_pin_Red, GPIO.OUT, initial=0)
        GPIO.setup(LED_pin_Green, GPIO.OUT, initial=0)
        GPIO.setup(LED_pin_Blue, GPIO.OUT, initial=0)

        for i in range(0, 5):
            GPIO.output(LED_pin_Red, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_pin_Red, GPIO.LOW)
            time.sleep(1)
            GPIO.output(LED_pin_Green, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_pin_Green, GPIO.LOW)
            time.sleep(1)
            GPIO.output(LED_pin_Blue, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_pin_Blue, GPIO.LOW)
            time.sleep(1)
            print(str(i))
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
    main()
