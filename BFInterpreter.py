
loopStartPos = 0
loopEndPos = 0


def filter(source):
    chars = []
    for char in source:
        if(char in ['<', '>', '+', '-', '[', ']', '.', ',']):
            chars.append(char)
    return chars


def execute():
    code = filter(',.')
    output = ''
    cells = [0]
    curPos = 0
    x = 0
    global loopStartPos
    global loopEndPos
    while x < len(code):
        cmd = code[x]
        if cmd == '<': 
            curPos = 0 if curPos <= 0 else curPos - 1
        if cmd == '>': 
            curPos = curPos + 1
            if curPos >= len(cells): cells.append(0)
        if cmd == '+':
            cells[curPos] = cells[curPos] + 1
        if cmd == '-':
            cells[curPos] = cells[curPos] - 1
        if cmd == '[':
            loopStartPos = x
        if cmd == ']':
            if cells[curPos] <= 0: 
                x = x + 1
                continue
            loopEndPos = x
            x = loopStartPos
        if cmd == '.':
            output = output + chr(cells[curPos])
        if cmd == ',':
            inVal = input('')
            cells[curPos] = ord(inVal[0])
        x = x + 1
    print(output)


if __name__ == '__main__':
    execute()
