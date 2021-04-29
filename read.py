file = open("2.png", 'rb')
png = []
CHUNKSIZE = 4

while True:
    byte = file.read(CHUNKSIZE) # tu 1= jeden bajt wedlug stack
    #print(byte)
    png.append(byte)
    if not byte:
        break

print(png)