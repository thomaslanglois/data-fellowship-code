if __name__ == "__main__":
    s = []
    while len(s) != 3:
        s = input('Enter 3 strings separated by a comma: ').split(',')
        if len(s) != 3:
            print('Sorry I really need 3 strings from you, not {}!'.format(len(s)))
    lengths = [len(l) for l in s]
    print(lengths)
    for length, first3, last3 in zip(lengths,[l[:3] for l in s], [l[-3:] for l in s]):
        print('len: {}, first 3: {}, last 3: {}'.format(length, first3, last3))