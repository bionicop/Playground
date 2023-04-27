import requests
from bs4 import BeautifulSoup

search_term = input("Enter your search term: ")
url = f"https://online-courses.club/?s={search_term}"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

courses = soup.find_all("article", {"class": "admania_gridpstlayt3"})

for course in courses:
    title = course.find("h2", {"class": "admania_entrytitle"}).text
    link = course.find("a", {"class": "admania_pstrdmr"})["href"]
    print(f"{title}: {link}\n")