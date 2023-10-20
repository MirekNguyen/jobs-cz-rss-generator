from app.controllers import ConfigController, FeedController, WebScrapeController

config = ConfigController()
jobs = WebScrapeController(config.data.get("url"))
feed = FeedController(config, jobs, config.args.output)
