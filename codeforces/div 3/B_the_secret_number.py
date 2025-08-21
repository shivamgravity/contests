def main():
    # code
    n = int(input())
    for _ in range(n):
        num = int(input())
        L = []
        for x in range(11,num):
            temp = x*10
            while temp < num:
                if x + temp == num:
                    L.append(x)
                temp *= 10
        print(len(L))
        L.sort()
        for x in L:
            print(x, end=" ")
        print()

if __name__ == '__main__':
    main()