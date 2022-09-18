import RPi.GPIO as GPIO
import time
import sys
import traceback


LED_pins = [19, 13, 6]


def init_LED(LED_pins):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_pins, GPIO.OUT, initial=0)


def blink_LED(curent_LED_pin):
    GPIO.output(curent_LED_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(curent_LED_pin, GPIO.LOW)
    time.sleep(1)


def main():
    try:
        init_LED(LED_pins)

        for i in range(0, 5):
            for LED_pin in LED_pins:
                blink_LED(LED_pin)
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
        print("CleanUp GPIO")
        GPIO.cleanup()
        print("End of program")


if __name__ == '__main__':
    main()
