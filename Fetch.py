import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def save_pages(url):
    # headers = {'User-Agent': 'Mozilla/5.0'}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }

    for i in range(10):  # Adjust range as needed
        page_url = url + "&start=" + str(i * 10)
        response = requests.get(page_url, headers=headers)

        if response.status_code == 404:
            raise Exception("Page not found")

        with open(f"page_{i+1}.html", "w", encoding="utf-8") as f:
            f.write(response.text)


url = 'https://scholar.google.com/scholar?q=(intitle%3Asurvey+OR+intitle%3Areview)+AND+(intitle%3Agrading+OR+intitle%3Aevaluation+OR+intitle%3Acorrection+OR+intitle%3Aassessment)+AND+(intitle%3Aprogramming+OR+intitle%3A"computer+science")+AND+(intext%3Aautomatic+OR+intext%3Aautomated+OR+intext%3Aautomating)+AND+(intext%3Astudent+OR+intext%3Alearn+OR+intext%3Aexam+OR+intext%3Aessay+OR+intext%3Aassignment)'

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-private')

driver = webdriver.Firefox(options=options)
driver.get('http://www.example.com')

# save the page source
page_source = driver.page_source

# write the page source to a file
with open('page.html', 'w') as f:
    f.write(page_source)

# close the browser
driver.quit()
# save_pages(url)
