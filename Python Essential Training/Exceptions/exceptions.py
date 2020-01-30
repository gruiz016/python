def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        # This raises and error to let user know what is wrong
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step


def main():
    # This try error is how you catch exceptions, block try lets the code excute and the except raises the error to end user.
    try:
        for i in inclusive_range(1, 2, 3, 25):
            print(i, end=' ', flush=True)
        print()
    except TypeError as e:
        print(f'range error: {e}')


if __name__ == '__main__':
    main()
