def main():
    # code
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        a = 1
        res = []
        while n // (1 + 10**a) >:
            if n % (1 + 10**a) != 0:
                a += 1
                continue
            res.append(n // (1 + 10**a))
            a += 1
        print(len(res))
        if len(res) > 0:
            res.sort()
            for x in res:
                print(x, end=" ")
            print()

if __name__ == '__main__':
    main() 
    