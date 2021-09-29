import sys
import traceback

from time import sleep
from re import findall
from subprocess import check_output


def get_temp():
    temp = check_output(["vcgencmd", "measure_temp"]).decode()
    temp = float(findall('\d+\.\d+', temp)[0])
    return(temp)


try:
    while True:
        temp = get_temp()
        print(temp)
        sleep(1)

except KeyboardInterrupt:
    # ...
    print('Exit pressed Ctrl+C')

except:
    # ...
    print("Other Exception")                        # Прочие исключения
    print("--- Start Exception Data:")
    traceback.print_exc(limit=2, file=sys.stdout)   # Подробности исключения через traceback
    print("--- End Exception Data:")

finally:
    # ...
    print('End of program')