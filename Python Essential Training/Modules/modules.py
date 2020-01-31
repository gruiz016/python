import sys


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))


if __name__ == '__main__':
    main()
