
# coding: utf-8

# In[ ]:


import re
import requests
import webbrowser
import urllib.request

def getHtml(url):    
    page = requests.get(url)
    html =page.text
    return html  

def mv(url,name):
    mvid = url.split('/')[-1]
    url = 'http://www.yinyuetai.com/insite/get-video-info?flex=true&videoId={}'.format(mvid)
    html = getHtml(url)
    reg = r'http://\w*?\.yinyuetai\.com/uploads/videos/common/.*?(?=&br)'
    pattern = re.compile(reg)
    findlist = re.findall(pattern,html)
    print(findlist)
    mvurl = findlist[-1]
    mp4 = mvurl.split('?')[0]
    mp4 = mp4[-4:]
    urllib.request.urlretrieve(mvurl,'{}{}'.format(name,mp4))
    
if __name__=='__main__':  
#     url = "http://v.yinyuetai.com/video/3191281"   
    url = input('请输入mv的url：')
    name = input('请输入歌名：')
    mv(url,name)  

