def main():
    sumofalpha = 0
    for i in range(32,128):
        print(f"{i}: " + chr(i))
        if chr(i).isalpha() and chr(i) == chr(i).upper():
            sumofalpha += i
    print(sumofalpha)

main()