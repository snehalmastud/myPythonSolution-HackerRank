def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    line = []
    for i in range(size):
        line.append(('-'.join(alphabet[size-1:i:-1]+alphabet[i:size])).center((1+2*(size-1)+2*(size-1)), '-'))
    print('\n'.join(line[:0:-1]+line))

