dFile = open("Data.txt", "r")
oFile = open("Output.txt", "w")

data = dFile.read()
for keyNumber in range(0, 26):
    newData = ""
    character = ""
    dontTouch = " ,\n.{}[]\'\""
    for i in range(len(data)):
        if data[i] in dontTouch:
            newData += data[i]
            continue
        counter = 0
        character = ord(data[i])
        while counter < keyNumber:
            character -= 1
            counter += 1
            if (chr(character)) == '@':
                character = ord('Z')
            elif (chr(character)) == '`':
                character = ord('z')
        newData += chr(character)
    oFile.write(f"Key #{keyNumber}:\n{newData}\n")
    oFile.write("______________________________________________________________________________________________________________________\n")
dFile.close()
oFile.close()
