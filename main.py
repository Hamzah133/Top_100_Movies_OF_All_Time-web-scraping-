from bs4 import BeautifulSoup
import requests

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup=BeautifulSoup(response.text,"html.parser")

headings=soup.findAll(name="h3")

print()

with open("movies.txt","w") as f:
    for heading in headings[::-1]:
        f.write(heading.getText()+"\n")