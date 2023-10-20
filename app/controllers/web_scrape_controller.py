from app.models import JobArticle, WebScrape


class WebScrapeController():
    def __init__(self, url):
        self.webscrape = WebScrape(url)
        self.data = self.find_data()
    def find_data(self):
        try:
            container = self.webscrape.soup.find(id="search-result-container")
            articles = container.find_all("article", class_="SearchResultCard")
            jobs = []
            for article in articles:
                job = self.extract_data(article)
                jobs.append(job)
            if not jobs:
                self.webscrape.trigger_error("Element with class 'SearchResultCard' not found.")
                return []
            return jobs
        except:
            self.webscrape.trigger_error("Element with class 'SearchResultCard' not found.")
            return

    def extract_data(self, article):
        try:
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
        except:
            self.webscrape.trigger_error("Attribute was not found.")
            return
        if not all([job_title, job_link, job_status, location, company_name]):
            self.webscrape.trigger_error("Article was not found.")
        job = JobArticle(
            job_title, job_link, job_status, location, company_name
        )
        return job
