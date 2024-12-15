def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif a == "" and int(b) >= 0:
        return b
    elif int(a) >= 0 and b == "":
        return a
    else:
        return str(int(a) + int(b))