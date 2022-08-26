def fel1():
    li = ['auto', 'villamos', 'metro']
    megoldas = [li[s].upper()+"!" for s in range(len(li))]
    print(megoldas)

def fel2():
    li = ['aladar', 'bela', 'cecil']
    megoldas = [s.capitalize() for s in li]
    print(megoldas)

def fel3():
    li = [0 for n in range(10)]
    print(li)

def fel4():
    li = [n + 1 for n in range(10)]
    megoldas = [n*2 for n in li]
    print(megoldas)

def fel5():
    li = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    megoldas = [int(s) for s in li]
    print(megoldas)

def fel6():
    li = "1234567"
    megoldas = [int(c) for c in li]
    print(megoldas)

def fel7():
    li = 'The quick brown fox jumps over the lazy dog'
    li = li.split(" ")
    megoldas = [len(s) for s in li]
    print(megoldas)

def fel8():
    li = "python is an awesome language"
    megoldas = [s[0] for s in li]
    print(megoldas)

def fel9():
    li = 'The quick brown fox jumps over the lazy dog'
    li = li.split(" ")
    megoldas = [(s, len(s)) for s in li]
    print(megoldas)

def fel10():
    li = [n for n in range(0,10,2)]
    print(li)

def fel11():
    li = [n**2 for n in range(0,20,2)]
    print(li)

def fel12():
    megoldas = []
    li = [n**2 for n in range(20)]
    for n in li:
        if n % 10 == 4:
            megoldas.append(n)
    print(megoldas)

def fel13():
    megoldas = [chr(n) for n in range(ord('A'), ord('Z'))]
    print(megoldas)

def fel14():
    li = [' apple ', ' banana ', ' kiwi']
    megoldas = [s.strip() for s in li]
    print(megoldas)

def fel15():
    li = [1, 0, 1, 1, 0, 1, 0, 0]
    megoldas = [str(s) for s in li]
    print("".join(megoldas))

fel1()
fel2()
fel3()
fel4()
fel5()
fel6()
fel7()
fel8()
fel9()
fel10()
fel11()
fel12()
fel13()
fel14()
fel15()