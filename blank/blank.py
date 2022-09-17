import sys
import traceback


def test(message):
    return print(message)


def main():
    try:
        test('Hello world!')

    except KeyboardInterrupt:
        # ...
        print('Exit pressed Ctrl+C')

    except Exception:
        # ...
        # Прочие исключения
        print('Other exception')
        print('--- Start Exception Data')
        # Подробности исключения через traceback
        traceback.print_exc(limit=2, file=sys.stdout)
        print('--- End Exception Data')

    finally:
        # ...
        print('End programm')


if __name__ == '__main__':
    main()
