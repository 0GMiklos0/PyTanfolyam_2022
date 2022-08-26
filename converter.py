def to_binary(n):
    hatvany = 0
    bin_szam = ""
    while n // (2 ** hatvany) >= 1:
        if(n // (2 ** hatvany) % 2 == 1):
            bin_szam += "1"
        else:
            bin_szam += "0"
        hatvany += 1
    return bin_szam[::-1]

def main():
    num = 186355
    print(to_binary(num))
    print(bin(num))

main()