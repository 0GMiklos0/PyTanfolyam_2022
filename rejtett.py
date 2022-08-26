def main():
    szoveg = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""
    megfejtes = ""
    for ch in szoveg:
        if ch.isalpha():
            if ch == "y":
                megfejtes += "a"
            elif ch == "z":
                megfejtes += "b"
            if ch == "Y":
                megfejtes += "A"
            elif ch == "Z":
                megfejtes += "B"
            else:
                megfejtes += chr(ord(ch)+2)
        else:
            megfejtes += ch
    print(megfejtes)

main()