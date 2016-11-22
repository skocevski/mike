import wget
import re
from urllib.parse import urlparse

print("\n Image URLs included in " + f )
def download_ALL(file, url):
    m = file.read()
    o= urlparse(url)
    host = o.netloc
    protocol = o.scheme

    #defininf regexp for img tags
    link = r'<img[^>]*\ssrc="(.*?)"'
    imgs = re.findall(link, str(m))

    i=0 #printing and download the images
    while(i<len(imgs)):
        img = imgs[i]
        if(img.find(protocol + "://" +host)==-1):
            img=protocol + "://"+ host + imgs[i]
        print(img)
        wget.download(img)
        i=i+1


f = input("Please enter the name of the local file ")
u = input("Please enter the URL, from this file was downloaded!")

download_ALL(f1, u)
f1=open(f, "r")