def searchIEND(png):
    length = len(png)
    position = 0
    for i in range(0, length):
        if png[i] == b'I':
            if png[i + 1] == b'E':
                if png[i + 2] == b'N':
                    if png[i + 3] == b'D':
                        position = i
                        break
    return position

def chunkIEND(png):
    position = searchIEND(png)
    if position == 0:
        print("Plik nie posiada chunk IEND")
        return -1
    else:
        print("Plik posiada chunk IEND")
        tmp = list(png[position - 1])
        if tmp[0] == 0:
            print("Pole danych puste. Strumień danych zakończony prawidłowo")
            return 1
        else:
            print("Pole danych nie jest puste")
            return -1
