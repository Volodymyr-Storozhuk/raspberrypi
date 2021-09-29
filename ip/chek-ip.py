import os                                               # Импортируем библиотеку по работе с ОС
import sys
import traceback
from re import findall                                  # Импортируем библиотеку по работе с регулярными выражениями


def get_local_ip(interface):
    if interface == 'eth0':
        local_ip = os.popen("ifconfig eth0 | grep inet").readline()
    if interface == 'wlan0':
        local_ip = os.popen("ifconfig wlan0 | grep inet").readline()
    if len(local_ip) > 0:
        local_ip = findall('\d+\.\d+.\d+.\d+', local_ip)[0]
    else:
        local_ip = 'disconnect'
    return(local_ip)


try:
    cur_eth_ip = get_local_ip("eth0")
    print('eth0:  ', cur_eth_ip)
    cur_wlan_ip = get_local_ip("wlan0")
    print('wlan0: ', cur_wlan_ip)

except KeyboardInterrupt:
    # ...
    print("Exit pressed Ctrl+C")                        # Выход из программы по нажатию Ctrl+C
except:
    # ...
    print("Other Exception")                            # Прочие исключения
    print("--- Start Exception Data:")
    traceback.print_exc(limit=2, file=sys.stdout)       # Подробности исключения через traceback
    print("--- End Exception Data:")
finally:
    print("End of program")                             # Информируем о завершении работы программы
