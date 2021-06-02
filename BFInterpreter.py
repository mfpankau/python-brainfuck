cells = [0]
curPos = 0

def filter(source):
    chars = []
    for char in source:
        if(char in ['<', '>', '+', '-', '[', ']', '.', ',']):
            chars.append(char)
    return chars


def execute():
    code = filter('jugwengbs.wrb,rbs[]<fsebg>')
    for cmd in code:
        if cmd == '<': 
            curPos = 0 if curPos <= 0 else curPos - 1
        if cmd == '>': 
            curPos = curPos + 1
            if curPos >= len(cells): cells.append(0)

if __name__ == '__main__':
    execute()
