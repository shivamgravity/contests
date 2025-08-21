def main():
    # code
    n = int(input())
    for _ in range(n):
        n1 = int(input())
        word = input()
        n2 = int(input())
        to_add = input()
        who = input()

        for x in range(n2):
            if who[x] == "V":
                word = to_add[x] + word
            else:
                word += to_add[x]
        
        print(word)

if __name__ == '__main__':
    main()