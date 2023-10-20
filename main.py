import argparse

from classes.models.config import Config
from classes.controllers.feed_controller import FeedController
from classes.controllers.web_scrape_controller import WebScrapeController


parser = argparse.ArgumentParser(description="Create RSS feed from web scraping")
parser.add_argument("-o", "--output", help="Specify output file name", required=True)
parser.add_argument("-c", "--config", help="Specify configuration file location", default='config/config.json')
args = parser.parse_args()

config = Config(args.config)
jobs = WebScrapeController(config.data.get("url"))
feed = FeedController(config, jobs.find_data(), args.output)
