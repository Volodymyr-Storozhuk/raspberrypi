import RPi.GPIO as GPIO                           # Импортируем библиотеку по работе с GPIO
import time                                       # Импортируем класс для работы со временем
import sys
import traceback                                  # Импортируем библиотеки для обработки исключений


def main():
    try:
        # Инициализация пинов
        LED_pin_PWM = 19
        GPIO.setmode(GPIO.BCM)                         # Выбираем режим нумерации пинов
        GPIO.setup(LED_pin_PWM, GPIO.OUT)              # Устанавливаем pinPWM в режим OUTPUT

        pwm = GPIO.PWM(LED_pin_PWM, 100)               # создаем ШИМ-объект для пина pinPWM с частотой 100 Гц
        pwm.start(10)                                  # Запускаем ШИМ на пине со скважностью 10% (0-100%)
        #                                              # Можно использовать данные типа float - 49.5, 2.45
        pwm.ChangeFrequency(1000)                      # Изменяем частоту до 10 КГц (также можно float)

        while 1:
            for i in range(0, 101):
                pwm.ChangeDutyCycle(i)                 # Изменяем коэффициент запонения (скважность) от 0 до 100%
                time.sleep(0.2)                        # Пауза на 0,1 сек
            time.sleep(5)                              # Пауза на 5 сек, для осциллографа
            for i in range(100, -1, -1):
                pwm.ChangeDutyCycle(i)                 # Изменяем коэффициент запонения (скважность) от 100 до 0%
                time.sleep(0.2)                        # Пауза на 0,1 сек
            time.sleep(5)                              # Пауза на 5 сек, для осциллографа

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
        # ...
        pwm.stop()                                     # Останавливаем ШИМ - необязательно
        print("CleanUp")                               # Информируем сбросе пинов
        GPIO.cleanup()                                 # Возвращаем пины в исходное состояние
        print("End of program")                        # Информируем о завершении работы программы


if __name__ == '__main__':
    main()
