import sys

def first():
    if len(sys.argv) == 3:
        num1, num2 = sys.argv[1], sys.argv[2]
        print(num1 + num2)
    else:
        print("Nem helyesen adta meg a szamokat")
        sys.exit(1)

def second():
    nums = int(input("Adjon meg ket szamot: "))
    if len(nums) == 2:
        print(sum(nums))
    else:
        print("Nem helyesen adta meg a szamokat")

first()
second()