def palindrom(s1):
    i = 1
    while s1[i-1] == s1[-i]:
        if i >= round(len(s1)/2):
            return f"{s1} palindrom"
        i += 1
    return f"{s1} nem palindrom"

def main():
    words = ["hey", "perec", "kerek", "gomba"]
    for par in words:
        print(palindrom(par))

main()