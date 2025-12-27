def swap_case(s):
    x = list(s)
    rec = []
    for i in x:

        if i.islower():
            f = i.upper()

            rec.append(f)
        else:
            f = i.lower()
            rec.append(f)
    string = ''.join(rec)
    return string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)