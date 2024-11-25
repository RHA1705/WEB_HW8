from models import Author, Quote
import connect
import json


with open('authors.json', 'r') as a:
    authors_data = json.load(a)

with open('qoutes.json', 'r') as f:
    quotes_data = json.load(f)

for author_data in authors_data:
    authors = Author(**author_data)
    authors.save()

for quote_data in quotes_data:
    author = Author.objects(fullname=quote_data['author']).first()
    quotes = Quote(tags=quote_data['tags'], author=author, quote=quote_data['quote'])
    quotes.save()
