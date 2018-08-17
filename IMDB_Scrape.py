import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.imdb.com/search/title?groups=top_250&sort=user_rating'


#grab the page and read its details

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


#parse the page
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"lister-item-content"})
container = containers[0]

filename = "movies.csv"
f = open(filename,"w")

headers = "MovieName,Votes,Gross,Rating \n"
f.write(headers)

for container in containers :
    movie_headers = container.findAll("h3",{"class" : "lister-item-header"})
    movie_names = movie_headers[0].a.text

    first_votes = container.find('span', attrs={'name': 'nv'})
    votes = first_votes['data-value']

    rating = container.strong.text

    print("Name of movie :" + movie_names)
    print("Votes :" + votes)
    print("Ratings :" + rating + "\n \n " )

    f.write(movie_names + "" + votes + "" + "rating" + "\n")

f.close()