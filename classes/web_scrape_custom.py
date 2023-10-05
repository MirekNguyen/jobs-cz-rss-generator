from classes.web_scrape import WebScrape
from classes.job_article import JobArticle


class WebScrapeCustom(WebScrape):
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