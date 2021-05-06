from Chunk import Chunk
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

class iTXt(Chunk):
    def __init__(self, keyword=None, compressionFlag=None, compressionMethod=None, languageTag=None,
                 translateKeyword=None, text=None):
        self.keyword = keyword
        self.compressionFlag = compressionFlag
        self.compressionMethod = compressionMethod
        self.languageTag = languageTag
        self.translateKeyword = translateKeyword
        self.text = text

    def __str__(self):
        tmp = self.keyword
        keyword = tmp.decode("utf-8")
        tmp2 = self.text
        text = tmp2.decode("utf-8")
        return "%s : %s" % (keyword, text)

    def chunkiTXt(self, png):
        start = 0
        number = 0
        position = 0
        while position != -1:
            keyword = ""
            text = ""
            position = super(iTXt, self).search(png, start, len(png), b'i', b'T', b'X', b't')

            if position == -1:
                if number == 0:
                    print("Chunk iTXt nie istnieje")
                    return -1
                return 0
            length = super(iTXt, self).lengthChunk(png, position)
            t = position + 4
            index = -1
            for i in range(t, t + length):
                if png[i + 1] == b'\x00':
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

            flag = int.from_bytes(png[index + 1], byteorder='big', signed=True)
            method = int.from_bytes(png[index + 2], byteorder='big', signed=True)

            index2 = -1
            for i in range(index+2, t + length):
                if png[i + 1] == b'\x00':
                    index2 = i + 1
                    languageTag = None
                    break

            if index2-index > 3:
                tmpLG = []
                for i in range(index+3, index2):
                    a = png[i]
                    if len(tmpLG) == 0:
                        tmpLG.append(a)
                        languageTag = tmpLG[0]
                    else:
                        languageTag = b''.join([tmpLG[0], a])
                        tmpLG.insert(0, languageTag)

            index3 = -1
            for i in range(index2, t + length):
                if png[i + 1] == b'\x00':
                    index3 = i + 1
                    translatedKeyword = None
                    break

            if index3-index2 > 1:
                tmpTK = []
                for i in range(index2+1, index3):
                    a = png[i]
                    if len(tmpTK) == 0:
                        tmpTK.append(a)
                        translatedKeyword = tmpTK[0]
                    else:
                        translatedKeyword = b''.join([tmpTK[0], a])
                        tmpTK.insert(0, translatedKeyword)

            tmpTXT = []
            for i in range(index3+1, t + length):
                a = png[i]
                if len(tmpTXT) == 0:
                    tmpTXT.append(a)
                    text = tmp[0]
                else:
                    text = b''.join([tmpTXT[0], a])
                    tmpTXT.insert(0, text)

            object = iTXt(keyword, flag, method, languageTag, translatedKeyword, text)

            if keyword == b'XML:com.adobe.xmp':
                xmpAsXML = BeautifulSoup(text, "lxml")
                print(xmpAsXML.prettify())
            else:
                print(object)



            start = position + 4
            number = number + 1
