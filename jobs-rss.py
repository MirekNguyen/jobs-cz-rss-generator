import pytz
import requests
from bs4 import BeautifulSoup

url = "https://www.jobs.cz/prace/praha/?q%5B%5D=PHP&date=24h&locality%5Bradius%5D=0"
timezone = pytz.timezone("Europe/Prague")
feed_id = "https://genshin-impact.fandom.com/wiki/Version"
feed_title = "Genshin versions"
feed_subtitle = "Genshin versions"
feed_link_href = "https://genshin-impact.fandom.com/wiki/Version"

class JobArticle:
    def __init__(self, job_title, job_link, job_status, location, company_name):
        self.job_title = job_title
        self.job_link = job_link
        self.job_status = job_status
        self.location = location
        self.company_name = company_name
    def print(self):
        print("Job Title:", self.job_title)
        print("Job Link:", self.job_link)
        print("Job Status:", self.job_status)
        print("Company Name:", self.company_name)
        print("Location:", self.location)
        print("----")


class WebScrapeData:
    def find_data(self):
        pass

    def trigger_error(self, err_message):
        self.has_error = True
        self.err_message = err_message

    def __init__(self, url):
        self.has_error = False
        response = requests.get(url)
        self.soup = BeautifulSoup(response.content, "html.parser")
        self.target_tables = self.find_data()

class WebScrapeCustom(WebScrapeData):
    def find_data(self):
        container = self.soup.find(id='search-result-container')
        if container:
            articles = container.find_all('article', class_='SearchResultCard')
            for article in articles:
                self.extract_data(article)
        else:
            self.trigger_error("Element with ID 'search-result-container' not found.")
    def extract_data(self, article):
        if article:
            # Extract data from the <article> element
            job_title = article.find('h2', class_='SearchResultCard__title').text.strip()
            job_link = article.find('a', class_='SearchResultCard__titleLink')['href']
            job_status = article.find('div', class_='SearchResultCard__status').text.strip()
            location = article.find('li', class_='SearchResultCard__footerItem',attrs={'data-test': 'serp-locality'}).text.strip()
            company_name = article.find('li', class_='SearchResultCard__footerItem').text.strip()
            if job_title and job_link and job_status and location and company_name:
                job = JobArticle(job_title, job_link, job_status, location, company_name)
                job.print()
            else:
                self.trigger_error("Article attribute was not found.")
        else:
            self.trigger_error("Article was not found.")
        

jobs = WebScrapeCustom(url)
jobs.find_data()
