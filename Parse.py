from bs4 import BeautifulSoup
import requests

def get_doi(title, authors):
    url = "https://api.crossref.org/works"
    params = {"query.title": title, "query.author": authors}
    response = requests.get(url, params=params)
    data = response.json()

    if data['message']['total-results'] > 0:
        return data['message']['items'][0]['DOI']
    else:
        return "DOI not found"

# Example usage:
title = "Your Article Title"
authors = "Author1, Author2"
print(get_doi(title, authors))

class Article:
    def __init__(self, title, authors, year):
        self.title = title
        self.authors = authors
        self.year = year
class ArticleDoi:
    def __init__(self, title, authors, year, doi):
        self.title = title
        self.authors = authors
        self.year = year
        self.doi = doi

def parse_articles():
    articles = set()

    for i in range(10):  # Adjust range as needed
        with open(f'page_{i+1}.html', 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

            for record in soup.find_all('div', {'class': 'gs_ri'}):
                title = record.find('h3').text
                details = record.find('div', {'class': 'gs_a'}).text
                authors, rest = details.split(' - ', 1)
                year = rest.split(', ')[-1].split(' - ')[0]

                article = Article(title, authors, year)
                articles.add(article)

    return articles

articles = parse_articles()
articlesDois = [get_doi(a.title, a.authors) for a in articles]

for article in articlesDois:
    print(f"{article.title} by {article.authors} ({article.year}). {article.DOI}[DOI].")

