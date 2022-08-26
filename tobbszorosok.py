def main():
    osszeg = 0
    li = sum(n for n in range(0,1000,3)) + sum(n for n in range(0,1000,5)) - sum(n for n in range(0,1000,15))
    for n in range(1000):
        if n%3 == 0 or n%5 == 0:
            osszeg += n
    print(osszeg)
    print(li)

main()