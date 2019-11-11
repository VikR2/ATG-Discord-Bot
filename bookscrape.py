import requests
import os
import urllib.request
import time
import re
from bs4 import BeautifulSoup

from dotenv import load_dotenv

#Read .env file
load_dotenv()
current_chapter = os.getenv('LATEST_CHAPTER')

def check_zong(website):
    url = website
    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")
    new_tag = soup.find_all("div",class_="tit")

    chapter = str(new_tag)
    chapter = re.findall("第.*章",chapter)
    latest_chap_num = chapter[0].replace("第","").replace("章","")
    
    if (latest_chap_num > current_chapter):
        # Read in the file
        with open('.env', 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(current_chapter,latest_chap_num)

        # Write the file out again
        with open('.env', 'w') as file:
            file.write(filedata)

        discord_message = f"Rawout! Chapter: {latest_chap_num}"
    else:
        discord_message = f"Current Raw: {chapter[0]} "

    return discord_message

print(check_zong("http://book.zongheng.com/book/408586.html"))