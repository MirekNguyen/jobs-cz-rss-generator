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
