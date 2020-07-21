Simple Web Scraping on IMDb Movie site using BeautifulSoup in Python :

Two packages are used :
  1. requests for performing your HTTP requests
  2. BeautifulSoup4 for handling all of your HTML processing
  
At first,web requests are made to the required page using "requests.get()" function which gives the raw HTML content of the webpage requested. Then we can extract the elements from the raw HTML using  "BeautifulSoup".
In this code,we are interested in finding the top rated movies with maximum votes and rating.So an empty file s created which lists the following categories : "MovieName","Votes","Gross","Rating". 

