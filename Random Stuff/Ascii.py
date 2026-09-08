countalpha = 0
countdigit = 0
countspesh = 0


def printascii():
    for i in range(32, 126):
        count = i
        if (chr(i).isalpha()):
            print(f"{chr(i)}")
    for i in range(32, 126):
        count = i
        if (chr(i).isdigit()):
            print(chr(i))
        else:
            print(chr(i))
    for i in range(32, 126):
            count = i
            if (chr(i).isdigit()):
                pass
            if (chr(i).isalpha()):
                pass
            else:
                print(i)
                

print(printascii())


    

