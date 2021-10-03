

def join_to_text(lst):
    for i in range(0,len(lst)):
        lst[i] = "".join(lst[i])
    lst = " ".join(lst)
    return lst



def main(text_ascii):
    new_text = []
    for i in range(0,len(text_ascii)):
        for j in range(0,len(text_ascii[i])):
            new_line = []
            if ord(text_ascii[i][j])<128:
                new_line.append(chr(128 - ord(text_ascii[i][j])))
            else:
                pass
        new_text.append(new_line)        
    new_text = join_to_text(new_text)
    print(new_text[::-1])





if __name__ == "__main__":
    text = open("sampletext.txt", "r",encoding='utf-8')
    main(text.read())
    
    