import requests_html
import pandas as pd
import urllib.request
import os
from os import walk
import requests

def getDownloadedFiles(directory: str) -> list:
    f = []
    for (dirpath, dirnames, filenames) in walk(directory):
        f.extend(filenames)
        break
    return f



def getHTML(url):
    session = requests_html.HTMLSession()
    r = session.get(url)
    r.html.render(sleep=5)
    return r.html

def download(link, folder, file, format):
    response = requests.get(link)
    with open(os.path.join(folder, file+"."+format), 'wb') as f:
        f.write(response.content)

page_url = 'https://fantasyoverlord.com/FPL/History'
page = getHTML(page_url)
directory = "Downloads"
document = page.find("div.col-md-12", first=True).find("ul", first=True).find("li")
files = getDownloadedFiles(directory)

for li in document:
    link = page_url+"?file="+li.text
    if (li.text+".csv" in files):
        print(li.text, "already exists")
    else:
        print("downloading", li.text)
        download(link, directory, li.text, "csv" )
        print("file saved")


