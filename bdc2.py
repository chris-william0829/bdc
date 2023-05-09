import pymssql
import datetime
import random
import webbrowser

url="http://dict.youdao.com/dictvoice?type=1&audio="

connect = pymssql.connect(host='127.0.0.1',server='n',port='1433',user='sa',password='xiongda123+A',database='Words')
cursor = connect.cursor()
cursor.execute('SELECT * FROM Sheet2$ where times = 0 and flag = 1')
words = cursor.fetchall()
cursor.execute("SELECT * FROM Sheet2$ where times <> 0 and flag = 1")
rows = cursor.fetchall()
for row in rows:
    cursor.execute("update Sheet2$ set times = '%f' where word = '%s'" %(((row[3]+1)%row[2]),row[0]))
connect.commit()
goal = min(200,len(words))
print(len(words))    
date = datetime.date.today()
output = str(date.year)+"-"+str(date.month)+"-"+str(date.day)+".txt"
output2 = str(date.year)+"-"+str(date.month)+"-"+str(date.day)+".dat"
outputfile = open(output,"a+")
outputfile2 = open(output2,"a+")
randomList = random.sample(range(0,len(words)),goal)
flag = True
i = 1
for num in randomList:
    pronunciation=url+words[num][0]
    webbrowser.open(pronunciation)
    print("No.%d" %i)
    while flag:
        cursor.execute("update Sheet2$ set times = '%f' where word = '%s'" %(words[num][3]+1,words[num][0]))
        command=input()
        if command == "y":
            cursor.execute("update Sheet2$ set Mem = '%d' where word = '%s'" %(words[num][4]+1,words[num][0]))
            break
        elif command == "r":
            webbrowser.open(pronunciation)
        elif command == "n":
            outputfile.write("%s %s\n" %(words[num][0],words[num][1].encode('latin1').decode('gbk')))
            outputfile2.write("%s\n" %(words[num][0]))
            break
        elif command == "s":
           print(words[num][0],words[num][1].encode('latin1').decode('gbk'))
    i=i+1
connect.commit()

