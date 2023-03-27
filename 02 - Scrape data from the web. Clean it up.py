import requests
from bs4 import BeautifulSoup

# Step 1: Scrape data from the web
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
text = soup.get_text()

# Step 2: Clean up the data
lines = text.split("\n")
cleaned_text = ""
for line in lines:
    if len(line.strip()) > 0:
        cleaned_text += line.strip() + " "
