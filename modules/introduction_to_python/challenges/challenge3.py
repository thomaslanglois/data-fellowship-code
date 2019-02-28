from datetime import datetime

if __name__ == "__main__":
    print('Rocket test: {}'.format(datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

    x = -1
    while x < 0:
        x = int(input('Enter a positive number: '))
        if x < 0:
            print('Sorry but the number has to be positive!')

    for i in range(x, -1, -1):
        print('{}'.format(i))
    print('Blast Off!')
    print('Rocket test: {}'.format(datetime.now().strftime("%Y/%m/%d %H:%M:%S")))
