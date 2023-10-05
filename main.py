import argparse

import pytz

from classes.config import Config
from classes.feed_custom import FeedCustom
from classes.web_scrape_custom import WebScrapeCustom


parser = argparse.ArgumentParser(description="Create RSS feed from web scraping")
parser.add_argument("-o", "--output", help="Specify output file name", required=True)
parser.add_argument("-c", "--config", help="Specify configuration file location", default='config/config.json')
args = parser.parse_args()

config = Config(args.config)
url = config.data.get("url")
timezone = pytz.timezone(config.data.get("timezone"))
feed_id = config.data.get("feed_id")
feed_title = config.data.get("feed_title")
feed_subtitle = config.data.get("feed_subtitle")
feed_link_href = config.data.get("feed_link_href")
jobs = WebScrapeCustom(url)
feed = FeedCustom(feed_id, feed_title, feed_subtitle, feed_link_href, jobs, args.output)
