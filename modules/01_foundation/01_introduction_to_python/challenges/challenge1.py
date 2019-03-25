if __name__ == "__main__":
    x = 0
    while x == 0:
        x, y = list(map(int, input('Enter two whole numbers separated by a space: ').split()))
        if x == 0:
            print('The first number has to be greater than 0!')
    print('{} + {} = {}'.format(x, y, x + y))
    print('{} - {} = {}'.format(x, y, x - y))
    print('{} * {} = {}'.format(x, y, x * y))
    print('{} / {} = {}'.format(y, x, y / x))

