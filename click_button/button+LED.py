import time
import sys
import traceback
import RPi.GPIO as GPIO

# Секція ініціалізації змінних
pinBtn = 24
pinLED = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBtn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinLED, GPIO.OUT, initial=0)


# Секція функцій і класів defs, class
def main():
    try:
        # якщо потрібно постійно виконувати код до преривання программи через Ctrl+C
        while True:
            statusPinBtn = GPIO.input(pinBtn)
            print(statusPinBtn)
            if statusPinBtn == 1:
                GPIO.output(pinLED, GPIO.HIGH)
            else:
                GPIO.output(pinLED, GPIO.LOW)
            time.sleep(0.5)

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
