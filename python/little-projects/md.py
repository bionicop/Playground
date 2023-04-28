import requests
from bs4 import BeautifulSoup
import re
import random

def extract_mediafile_links(course_url):
    response = requests.get(course_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    links = soup.find_all("a", href=re.compile("^https://mediafile\.cc/"))
    links = [link for link in links if link['href'] != 'https://mediafile.cc/upgrade/2']
    tmp_file_name = f"tmp_{random.randint(1000, 9999)}_{len(links)}.txt"
    
    with open(tmp_file_name, "w") as f:
        for link in links:
            f.write(link["href"] + "\n")
    
    return tmp_file_name