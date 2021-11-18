import requests
from bs4 import BeautifulSoup


def krebs():
    url = "https://krebsonsecurity.com"
    r1 = requests.get(url)
    coverpage = r1.content
    soup1 = BeautifulSoup(coverpage, features="html.parser")
    coverpage_news = soup1.find("h2", class_="entry-title")
    headline = coverpage_news.get_text()
    coverpage_desc = soup1.find("p")
    description = coverpage_desc.get_text()
    post_url = coverpage_news.findChild("a")["href"]
    author = "KrebsOnSecurity"
    date = soup1.find("span", class_="date updated").get_text()
    print(post_url)
    blog = {"headline": headline.strip(), "description": description, "url": url, "post_url": post_url, "author": author, "date": date}
    return blog
