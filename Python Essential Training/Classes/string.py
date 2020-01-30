class RevStr(str):
    # Overrideing __str__ method it inhertited.
    def __str__(self):
        return self[::-1]


def main():
    hello = RevStr('Hello, World.')
    print(hello)


if __name__ == '__main__':
    main()
