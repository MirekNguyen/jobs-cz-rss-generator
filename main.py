import pytz
import argparse

from classes.feed_custom import FeedCustom
from classes.web_scrape_custom import WebScrapeCustom

url = "https://www.jobs.cz/prace/praha/?q%5B%5D=PHP&date=3d&locality%5Bradius%5D=0"
timezone = pytz.timezone("Europe/Prague")

feed_id = "https://www.jobs.cz/prace/praha/?q%5B%5D=PHP&date=3d&locality%5Bradius%5D=0"
feed_title = "Jobs"
feed_subtitle = "Jobs"
feed_link_href = (
    "https://www.jobs.cz/prace/praha/?q%5B%5D=PHP&date=24h&locality%5Bradius%5D=0"
)

parser = argparse.ArgumentParser(description="Description of your script")
parser.add_argument("-o", "--output", help="Specify output file name", required=True)
args = parser.parse_args()

jobs = WebScrapeCustom(url)
feed = FeedCustom(feed_id, feed_title, feed_subtitle, feed_link_href, jobs, args.output)


