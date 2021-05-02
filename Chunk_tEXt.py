from Chunk import Chunk


class tEXt(Chunk):
    def __init__(self, keyword=None, text=None):
        self.keyword = keyword
        self.text = text

    def __str__(self):
        tmp = self.keyword
        keyword = tmp.decode("utf-8")
        tmp2 = self.text
        text = tmp2.decode("utf-8")
        if str(keyword).startswith("EXIF"):
            keyword = keyword[5:]
        return "%s :  %s" % (keyword, text)

    def chunktEXt(self, png):
        keyword = ""
        text = ""
        position = super(tEXt, self).searchChunk(png, b't', b'E', b'X', b't')
        if position == -1:
            print("Chunk tEXt nie istnieje")
            return -1
        length = super(tEXt, self).lengthChunk(png, position)
        t = position + 4
        index = -1
        for i in range(t, t + length):
            if png[i+1] == b'\x00':
                index = i + 1
                break
        tmp = []
        for i in range(t, index):
            a = png[i]
            if len(tmp) == 0:
                tmp.append(a)
                keyword = tmp[0]
            else:
                keyword = b''.join([tmp[0], a])
                tmp.insert(0, keyword)

        tmp_text = []
        for i in range(index+1, t + length):
            a = png[i]
            if len(tmp_text) == 0:
                tmp_text.append(a)
                text = tmp_text[0]
            else:
                text = b''.join([tmp_text[0], a])
                tmp_text.insert(0, text)

        object = tEXt(keyword, text)
        print(object)
        return object