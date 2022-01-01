# goodreadsQuotesScrap
python script to scrap tagged-quotes from Goodreads, run it as follows:

        python3 scrap_goodreads_quotes_en.py

#### Before Running:
* Good understanding of python and mongodb is important.
* Install mongodb python driver with the following command:

        pip install pymongo     
#### 2 Example Quotes:

```json

{ 
  "text":"May you live every day of your life",
  "author":"Jonathan Swift"
  "tags":
  [
    "inspirational",
    "life",
    "philosophy",
    "wisdom"
  ]
}
,
{
  "text":"That's what literature is. It's the people who went before us, tapping out messages from the past, from beyond the grave, trying to tell us about life and death! Listen to them",
  "author":"Connie Willis",
  "book":"Passage",
  "tags":
  [
    "death",
    "life",
    "literature",
    "messages"
  ]
}
```


#### Referneces:
 - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library for web-scrapping
 - [urllib.request.urlopen](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen) module for opening URLs
 - [pymongo](https://pymongo.readthedocs.io/en/stable/api/pymongo/index.html)
