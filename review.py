import pymssql
import datetime
import random
import webbrowser

def find(word,trans):
    s = word.split("\n")[0]
    for it in trans:
        if s in it:
            print(it.split("\n")[0])


if __name__ == '__main__':
    date = datetime.date.today()
    output = '2021-12-10.txt'
    output2 = '2021-12-10.dat'
    inputfile = open(output2,"r")
    tran = open(output,"r")
    words = inputfile.readlines()
    trans = tran.readlines()
    url="http://dict.youdao.com/dictvoice?type=1&audio="
    randomList = random.sample(range(0,len(words)),len(words))
    flag = True
    i = 1
    for num in randomList:
        pronunciation=url+words[num]
        webbrowser.open(pronunciation)
        print("No.%d" %i)
        while flag:
            command=input()
            if command == "y":
                break
            elif command == "r":
                webbrowser.open(pronunciation)
            elif command == "n":
                break
            elif command == "s":
                find(words[num],trans)
        i=i+1
    inputfile.close()