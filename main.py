import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

empire_page = response.text

soup = BeautifulSoup(empire_page,"html.parser")

movie_title =soup.find_all(name ="h3" , class_="title")

movie_titles = [movie.getText() for movie in movie_title]

new_movie_list = movie_titles[::-1]

print (new_movie_list)

with open("movies.txt" , mode ="w" , encoding="utf-8") as file:
    for movie in new_movie_list:
        file.write(f"{movie}\n")