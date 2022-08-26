def main():
    s = "magÁÁnhangzoök"
    for var in s:
        if var.lower() in "aáeéiíoóöőuúüű":
            s = s.replace(var, "")
    print(s)

main()