

if __name__ == '__main__':
    
    inputf = open("C:\\Users\\87039\\Desktop\\1998.txt","r")
    output = open("words.txt","a+")
    while True:
        line=inputf.readline()
        word=line.split('\n')
        
        if not line:
            break
        output.write("'%s',\n" % word[0])

    inputf.close()
    output.close()