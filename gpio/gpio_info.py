import RPi.GPIO as GPIO


def get_GPIO_info():
    print(f'GPIO VERSION: {GPIO.VERSION}')
    print('GPIO full info:')
    print(GPIO.RPI_INFO)
    print(f'REVISION: {GPIO.RPI_INFO["P1_REVISION"]}')
    print(f'REVISION: {GPIO.RPI_REVISION}')


def check_GPIO_mode():
    # GPIO.setmode(GPIO.BOARD)
    GPIO.setmode(GPIO.BCM)

    mode = GPIO.getmode()
    if mode == 10:
        print('GPIO.BOARD Mode')
    elif mode == 11:
        print('GPIO.BCM Mode')
    else:
        print(mode)


def main():
    # get_GPIO_info()
    check_GPIO_mode()


if __name__ == '__main__':
    main()
