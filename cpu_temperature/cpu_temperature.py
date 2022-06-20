import sys
import traceback

from time import sleep
from re import findall
from subprocess import check_output


def get_temp():
    temp = check_output(["vcgencmd", "measure_temp"]).decode()
    temp = float(findall(r'\d+\.\d+', temp)[0])
    return(temp)


try:
    while True:
        temp = get_temp()
        print('CPU temperature: ' + str(temp))
        sleep(1)

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
