# Youtube series: https://www.youtube.com/playlist?list=PLICW5UpCwEj3W06oupZkFc0MEYY6EAckX
# Documention: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import re   # regular expression

with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("input", type="text")
for tag in tags:
	tag['placeholder'] = "I changed you!"

# with open("changed.html", "w") as file:
# 	file.write(str(doc))