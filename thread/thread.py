from time import sleep, ctime


def loop0():
    print('start loop0 at:', ctime())
    sleep(4)
    print('loop0 down at:', ctime())


def loop1():
    print('start loop1 at:', ctime())
    sleep(4)
    print('loop1 down at:', ctime())


def main():
    print('start all at:', ctime())
    loop0()
    loop1()
    print('all down at:', ctime())


if __name__ == '__main__':
    main()
