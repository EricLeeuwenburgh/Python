# Youtube series: https://www.youtube.com/playlist?list=PLICW5UpCwEj3W06oupZkFc0MEYY6EAckX
# Documention: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests

# HTML from File
with open("data/index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

#print(doc)

# Search by HTML-tags
tags = doc.find_all("p")[0]

print(tags.find_all("b"))

# HTML From Website
url = "https://www.newegg.ca/msi-geforce-rtx-4070-ti-rtx-4070-ti-gaming-x-trio-12g/p/N82E16814137771?Item=N82E16814137771"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent			# Get parent from '$'
strong = parent.find("strong")		# Select label <strong> from parent
print(strong.string)				# Select only the string/text

'''
Note: 	Some websites / companies have build in protection from HTML requests by bots, like: Amazon. Scraping won't work on those website.
		There are legal rules for scraping websites. Do not use this skill in large amount before reading up on the legal matters. 
'''