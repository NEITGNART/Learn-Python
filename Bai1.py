

def solve():

    bistring = list('1111111')
    n = len(bistring)
    i = n - 1
    while (i >= 0 and bistring[i] == '1'):
        i -= 1

    if i < 0:
        for i in range(n):
            print(0, end = '')
    else:
        bistring[i] = '1'
        for j in range(i + 1, n):
            bistring[j] = '0'

        for j in range(n):
            print(bistring[j], end = '')
    # other solution, just convert to binary to int, then + 1 and print

def main():
    solve()

if __name__ == '__main__':
    main()
