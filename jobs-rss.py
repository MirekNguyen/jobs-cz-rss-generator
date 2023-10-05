import sys

import pytz
import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator

url = "https://www.jobs.cz/prace/praha/?q%5B%5D=PHP&date=3d&locality%5Bradius%5D=0"
timezone = pytz.timezone("Europe/Prague")
feed_id = "https://genshin-impact.fandom.com/wiki/Version"
feed_title = "Jobs"
feed_subtitle = "Jobs"
feed_link_href = (
    "https://www.jobs.cz/prace/praha/?q%5B%5D=PHP&date=24h&locality%5Bradius%5D=0"
)


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
        self.data = self.find_data()


class WebScrapeCustom(WebScrapeData):
    def find_data(self):
        container = self.soup.find(id="search-result-container")
        if container:
            articles = container.find_all("article", class_="SearchResultCard")
            jobs = []
            for article in articles:
                job = self.extract_data(article)
                jobs.append(job)
            return jobs
        else:
            self.trigger_error("Element with ID 'search-result-container' not found.")

    def extract_data(self, article):
        if article:
            # Extract data from the <article> element
            job_title = article.find(
                "h2", class_="SearchResultCard__title"
            ).text.strip()
            job_link = article.find("a", class_="SearchResultCard__titleLink")["href"]
            job_status = article.find(
                "div", class_="SearchResultCard__status"
            ).text.strip()
            location = article.find(
                "li",
                class_="SearchResultCard__footerItem",
                attrs={"data-test": "serp-locality"},
            ).text.strip()
            company_name = article.find(
                "li", class_="SearchResultCard__footerItem"
            ).text.strip()
            if job_title and job_link and job_status and location and company_name:
                job = JobArticle(
                    job_title, job_link, job_status, location, company_name
                )
                return job
            else:
                self.trigger_error("Article attribute was not found.")
        else:
            self.trigger_error("Article was not found.")


class Feed:
    def __init__(self):
        self.fg = FeedGenerator()
        self.fg.id(feed_id)
        self.fg.title(feed_title)
        self.fg.subtitle(feed_subtitle)
        self.fg.link(href=feed_link_href, rel="self")
        self.fg.language("en")
        pass

class FeedCustom(Feed):
    def __init__(self, data):
        super().__init__()
        for item in data.data:
            fe = self.fg.add_entry()
            fe.id(item.job_title)
            fe.title(item.job_status + ' | ' + item.company_name + ' | ' + item.job_title)
            fe.link(href=item.job_link, replace=True)
            fe.description(
                "Title: " + item.job_title + "<br>" +
                "Status: " + item.job_status + "<br>" +
                "Location: " + item.location + "<br>" +
                "Company: " + item.company_name
            )
        self.fg.rss_str(pretty=True)
        self.fg.rss_file('./jobs-rss.xml')



jobs = WebScrapeCustom(url)
feed = FeedCustom(jobs)
