import webbrowser 
import codecs
import time
import os

url = 'https://www.baidu.com/'

#判断网页地址是否有效
# 我本地的chrome浏览器文职
chromepath = 'C:\Users\xxx\AppData\Local\Google\Chrome\Application\chrome.exe'
# 注册浏览器对象
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
# 打开浏览器
webbrowser.get('chrome').open_new_tab('www.baidu.com')
#如果网页地址有效则打开网页
webbrowser.open(url)
time.sleep(15)
#然后关闭浏览器
os.system('taskkill /F /IM chrome.exe')