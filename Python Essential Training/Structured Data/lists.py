def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print_list(game)
    
    # Slice works like range with the first number is the start, end, and step by
    print(game[1:5:2])


def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


if __name__ == '__main__':
    main()
