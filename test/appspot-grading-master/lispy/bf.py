def bf(code):
        s = ""
        cPtr = ptr = 0
        while cPtr < len(code):
                matching = 0
                c = code[cPtr]
                if c == ">": ptr += 1
                if c == "<": ptr -= 1
                if c == "+": cells[ptr] = cells[ptr] + 1
                if c == "-": cells[ptr] = cells[ptr] - 1
                if c == ".": stdout.write(chr(cells[ptr]))
                if c == ",": cells[ptr] = ord(stdin.read(1))
                if c == "[" and cells[ptr] == 0:
                        for x in xrange(cPtr,len(code)):
                                if code[x] == '[': matching += 1
                                if code[x] == ']':
                                        if matching > 0: matching -= 1
                                        if matching == 0: cPtr = x; break
                if c == "]" and cells[ptr] != 0:
                        for x in xrange(cPtr,-1,-1):
                                if code[x] == ']': matching += 1
                                if code[x] == '[':
                                        if matching > 0: matching -= 1
                                        if matching == 0: cPtr = x; break
                cPtr += 1
