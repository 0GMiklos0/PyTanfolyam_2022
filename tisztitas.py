def main():
    ip_cim = "192.20.246.138:\n 6666"
    i = 0
    while ip_cim[i] != ":":
        i += 1
    new_str = ip_cim[i+1:]
    new_str = new_str.strip()
    ip_cim = ip_cim[:i+1]+new_str
    print(ip_cim)

main()