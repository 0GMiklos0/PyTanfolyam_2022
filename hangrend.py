def main():
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'
    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]
    for s1 in words:
        mely = False
        magas = False
        for s2 in s1:
            if s2 in MELY_MGHK:
                mely = True
            if s2 in MAGAS_MGHK:
                magas = True
        if mely and magas:
            print("Vegyes")
            continue
        elif mely:
            print("Mely")
            continue
        elif magas:
            print("Magas")
            continue

print(main())