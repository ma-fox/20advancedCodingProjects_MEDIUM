import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud

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

# Step 3: Load data into a data analysis tool (in this case, a word cloud)
# once the WordCloud object is created, it generates the word cloud image based
# on the frequency of words in the input text. The image can then be saved or
# displayed using matplotlib or other visualization libraries.

wordcloud = WordCloud(width=800, height=800,
                      background_color='white').generate(cleaned_text)
