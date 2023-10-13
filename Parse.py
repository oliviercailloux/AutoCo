# import requests
# from bs4 import BeautifulSoup

# def fetch_articles(url):
#     headers = {'User-Agent': 'Mozilla/5.0'}
    
#     for i in range(10):  # Adjust range as needed
#         page_url = url + "&start=" + str(i * 10)
#         response = requests.get(page_url, headers=headers)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         for record in soup.find_all('div', {'class': 'gs_ri'}):
#             title = record.find('h3').text
#             details = record.find('div', {'class': 'gs_a'}).text
#             # year = details.split('-')[-2].strip().split(',')[0]
#             year = details.split(', ')[-1].split(' - ')[0]

#             print(f"{title} ({year})")

# url = "https://scholar.google.com/scholar?q=(intitle%3Asurvey+OR+intitle%3Areview)+AND+(intitle%3Agrading+OR+intitle%3Aevaluation+OR+intitle%3Acorrection+OR+intitle%3Aassessment)+AND+(intitle%3Aprogramming+OR+intitle%3A\"computer+science\")+AND+(intext%3Aautomatic+OR+intext%3Aautomated+OR+intext%3Aautomating)+AND+(intext%3Astudent+OR+intext%3Alearn+OR+intext%3Aexam+OR+intext%3Aessay+OR+intext%3Aassignment)"
# fetch_articles(url)

# import requests
# from bs4 import BeautifulSoup

# class Article:
#     def __init__(self, title, year, doi):
#         self.title = title
#         self.year = year
#         self.doi = doi

# def fetch_articles(url):
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     articles = set()

#     for i in range(10):  # Adjust range as needed
#         page_url = url + "&start=" + str(i * 10)
#         response = requests.get(page_url, headers=headers)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         for record in soup.find_all('div', {'class': 'gs_ri'}):
#             title = record.find('h3').text
#             details = record.find('div', {'class': 'gs_a'}).text
#             year = details.split(', ')[-1].split(' - ')[0]
#             try:
#                 doi = record.find('div', {'class': 'gs_fl'}).find_all('a')[-1]['href']
#             except IndexError:
#                 doi = "DOI not found"

#             article = Article(title, year, doi)
#             articles.add(article)

#     return articles

# url = "https://scholar.google.com/scholar?q=(intitle%3Asurvey+OR+intitle%3Areview)+AND+(intitle%3Agrading+OR+intitle%3Aevaluation+OR+intitle%3Acorrection+OR+intitle%3Aassessment)+AND+(intitle%3Aprogramming+OR+intitle%3A\"computer+science\")+AND+(intext%3Aautomatic+OR+intext%3Aautomated+OR+intext%3Aautomating)+AND+(intext%3Astudent+OR+intext%3Alearn+OR+intext%3Aexam+OR+intext%3Aessay+OR+intext%3Aassignment)"
# articles = fetch_articles(url)

# for article in articles:
#     print(f"{article.title} ({article.year}). {article.doi}")

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

