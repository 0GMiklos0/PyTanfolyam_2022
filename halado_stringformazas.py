def main():
    col1 = ["NAME", "Miki", "Bori", "Zsofi"]
    col2 = ["AGE", "20", "17", "22"]
    col3 = ["SOCIAL CREDIT", "200", "500", "550"]
    for str in range(len(col1)):
        print("{0:<15} {1:^16} {2:>17}".format(col1[str], col2[str], col3[str], ))

main()