def main():
    li = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
    new_li = []
    for i in li:
        if i in new_li:
            continue
        else:
            new_li.append(i)
    print(new_li)

main()