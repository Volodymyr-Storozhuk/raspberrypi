import sys
import traceback
import os

from time import sleep
from re import findall
from subprocess import check_output


def get_cpu_temperature():
    cpu_temperature = check_output(["vcgencmd", "measure_temp"]).decode()
    cpu_temperature = float(findall(r'\d+\.\d+', cpu_temperature)[0])
    return cpu_temperature


def main():
    try:
        while True:
            os.system('clear')
            cpu_temperature = get_cpu_temperature()
            print('CPU temperature: ' + str(cpu_temperature))
            sleep(5)

    except KeyboardInterrupt:
        # ...
        print('Exit pressed Ctrl+C')

    except Exception:
        # ...
        # Прочие исключения
        print("Other Exception")
        print("--- Start Exception Data:")
        # Подробности исключения через traceback
        traceback.print_exc(limit=2, file=sys.stdout)
        print("--- End Exception Data:")

    finally:
        # ...
        print('End program')


if __name__ == '__main__':
    main()
