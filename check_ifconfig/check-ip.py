import os
import sys
import traceback

# Импортируем библиотеку по работе с регулярными выражениями
from re import findall


def get_local_ip(interface):
    if interface == 'eth0':
        # local_ip = os.popen("ifconfig eth0 | grep inet").readline()
        local_ip = os.popen("ip addr | grep inet | grep eth0").readline()
    if interface == 'wlan0':
        # local_ip = os.popen("ifconfig wlan0 | grep inet").readline()
        local_ip = os.popen("ip addr | grep inet | grep wlan0").readline()
    if len(local_ip) > 0:
        local_ip = findall(r'\d+\.\d+.\d+.\d+', local_ip)[0]
    else:
        local_ip = 'disconnect'
    return local_ip


def main():
    try:
        # Проверяю локальное подключение
        cur_eth_ip = get_local_ip("eth0")
        print('eth0:  ', cur_eth_ip)
        # Проверяю подключение по WiFi
        cur_wlan_ip = get_local_ip("wlan0")
        print('wlan0: ', cur_wlan_ip)
    except KeyboardInterrupt:
        # ...
        # Выход из программы по нажатию Ctrl+C
        print("Exit pressed Ctrl+C")
    except Exception:
        # ...
        # Прочие исключения
        print("Other Exception")
        print("--- Start Exception Data:")
        # Подробности исключения через traceback
        traceback.print_exc(limit=2, file=sys.stdout)
        print("--- End Exception Data:")
    finally:
        # Информируем о завершении работы программы
        print("End program")


if __name__ == '__main__':
    main()
