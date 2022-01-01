# -*- coding: utf-8 -*-
"""scrap goodreads quotes into mongo database
"""

"""**1. Import Libraries & Methods**"""

from pymongo import MongoClient
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen

"""**2. Connect to MongoDB**"""

mongo_client = MongoClient('Enter here your connection string - from Atlas UI')
db = mongo_client.goodreads  # create database object referencing the database you're connecting to (goodreads, for example)
db

"""**3. Prepare Base URL and inputs**"""

# Website URL as input 
BASE_URL = "https://www.goodreads.com/quotes"
# Some common tags
TAGS_EN = ['life', 'inspiration', 'spirituality', 'wisdom', 'human', 'motivation', 'love', 'truth', 'hope', 'faith',
           'time', 'life-lessons', 'music', 'heart', 'philosophy']

"""**4. Functions for Scrapping**"""


# please, understand the website you're scrapping before moving on, you can do this by 'inspect'
# extract quote text, author/book, tags
def extract_quote_details(containers):
    for c in containers:
        curr_quote = {}
        # list of tags
        quote_tags = c.find('div', class_="greyText smallText left")
        if quote_tags is not None:
            curr_quote['tags'] = [t.text for t in quote_tags.find_all('a')]
        # extract text, author, book(if exists)
        quote_text = c.find_all('div', class_="quoteText")[0]
        div_content = c.text.strip().split('\n')
        text = div_content[0].strip()[1:-2]
        if db.quotes.find({'text': text}).count() != 0:
            continue
        curr_quote['text'] = text
        author = quote_text.find_all('span', class_="authorOrTitle")[0].text.strip()
        book = quote_text.find('a', class_="authorOrTitle")
        if book is not None:
            book = book.text.strip()
            curr_quote['book'] = book
            curr_quote['author'] = author[0:-1]  # remove the , from the author span
        else:
            curr_quote['author'] = author
        # insert to the db
        db.quotes.insert_one(curr_quote)  # replace quotes with the name of the target collection


# Function to scrap quotes from all pages of a specified tag
def scrap_quotes(url, page_number=1):
    final_url = url + '?page=' + str(page_number)
    client = urlopen(final_url)  # Create client-based request performing the request (context manager)
    html = client.read()  # get HTML
    soup = BeautifulSoup(html, 'html.parser')  # HTML parser
    client.close()  # no further work with the connection, so close it
    quote_containers = soup.find_all('div', class_=r"quoteDetails ")
    if len(quote_containers) < 1:
        return
    extract_quote_details(quote_containers)


# scarp quotes from all common tags
def scrap_all_en():
    for tag in TAGS_EN:
        url = BASE_URL + '/tag/' + tag
        for i in range(1, 20):  # u may need to play with this
            scrap_quotes(url, i)


"""**5. Run Main Scrapping function**"""
scrap_all_en()
