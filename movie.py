# Python3 code for movie 
# recommendation based on 
# emotion 

# Import library for web 
# scrapping 

from bs4 import BeautifulSoup as SOUP 
from run import label
import re 
import requests as HTTP 

# Main Function for scraping 
def movie(emotion): 

	# IMDb Url for Drama genre of 
	# movie against emotion Sad 
	if(emotion == "sad"): 
		urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=popularity, asc'

	# IMDb Url for Musical genre of 
	# movie against emotion Disgust 
	elif(emotion == "disgust"): 
		urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=popularity, asc'

	# IMDb Url for Family genre of 
	# movie against emotion Anger 
	elif(emotion == "angry"): 
		urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=popularity, asc'

	# IMDb Url for Thriller genre of 
	# movie against emotion Happy
	elif(emotion == "happy"): 
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=popularity, asc'

	# IMDb Url for Sport genre of 
	# movie against emotion Fear 
	elif(emotion == "scared"): 
		urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=popularity, asc'

	# IMDb Url for Thriller genre of 
	# movie against emotion Enjoyment 
	elif(emotion == "happy"): 
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=popularity, asc'

	# IMDb Url for Western genre of 
	elif(emotion == "neutral"): 
		urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=popularity, asc'

	# IMDb Url for Film_noir genre of 
	# movie against emotion Surprise 
	elif(emotion == "surprised"): 
		urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=popularity, asc'

	# HTTP request to get the data of 
	# the whole page 
	response = HTTP.get(urlhere) 
	data = response.text 

	# Parsing the data using 
	# BeautifulSoup 
	soup = SOUP(data, "lxml") 

	# Extract movie titles from the 
	# data using regex 
	title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
	return title 

# Driver Function 
if __name__ == '__main__': 

	emotion = label
	a = movie(emotion) 
	count = 0
	if(emotion == "disgust" or emotion == "angry"
						or emotion=="surprised"): 

		for i in a: 

			# Splitting each line of the 
			# IMDb data to scrape movies 
			tmp = str(i).split('>;') 

			if(len(tmp) == 4): 
				print(tmp[1][:-4]) 

			if(count > 14): 
				break
			count += 1
	else: 
		for i in a: 
			tmp = str(i).split('>') 

			if(len(tmp) == 3): 
				print(tmp[1][:-3]) 

			if(count > 12): 
				break
			count+=1
