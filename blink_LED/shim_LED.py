import RPi.GPIO as GPIO
import time
import sys
import traceback


def main():
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        #  инициализация GPIO19 как выход
        GPIO.setup(19, GPIO.OUT)

        # частота 100Hz
        p = GPIO.PWM(19, 100)
        p.start(0)

        # while 1:
        #     for x in range(50):
        #         p.ChangeDutyCycle(x)
        #         time.sleep(0.1)

        for x in range(50):
            p.ChangeDutyCycle(50-x)
            time.sleep(0.1)

    except KeyboardInterrupt:
        # ...
        print("Exit pressed Ctrl+C")                   # Выход из программы по нажатию Ctrl+C
    except Exception:
        # ...
        print("Other Exception")                       # Прочие исключения
        print("--- Start Exception Data:")
        traceback.print_exc(limit=2, file=sys.stdout)  # Подробности исключения через traceback
        print("--- End Exception Data:")
    finally:
        print("CleanUp")                               # Информируем сбросе пинов
        p.stop()
        GPIO.cleanup()                                 # Возвращаем пины в исходное состояние
        print("End of program")


if __name__ == '__main__':
    main()
