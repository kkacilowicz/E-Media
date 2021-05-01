class Chunk:
    def searchChunk(self, png, x, y, z, t):
        length = len(png)
        position = -1
        for i in range(0, length):
            if png[i] == x:
                if png[i + 1] == y:
                    if png[i + 2] == z:
                        if png[i + 3] == t:
                            position = i
                            break
        return position

    def lengthChunk(self, png, position):
        a = png[position - 4]
        b = png[position - 3]
        c = png[position - 2]
        d = png[position - 1]
        e = b''.join([a, b, c, d])
        length = int.from_bytes(e, byteorder='big', signed=True)
        return length