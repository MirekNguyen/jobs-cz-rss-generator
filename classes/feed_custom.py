import locale
from datetime import datetime

import pytz

from classes.feed import Feed


class FeedCustom(Feed):
    def __init__(self, config, data, output_file):
        super().__init__(
            config.data.get("feed_id"),
            config.data.get("feed_title"),
            config.data.get("feed_subtitle"),
            config.data.get("feed_link_href"),
        )
        for item in data.data:
            fe = self.fg.add_entry()
            fe.id(item.job_title)
            fe.title(
                item.job_status + " | " + item.company_name + " | " + item.job_title
            )
            fe.link(href=item.job_link, replace=True)
            fe.description(
                "Title: "
                + item.job_title
                + "<br>"
                + "Status: "
                + item.job_status
                + "<br>"
                + "Location: "
                + item.location
                + "<br>"
                + "Company: "
                + item.company_name
            )
            locale.setlocale(locale.LC_TIME, config.data.get("locale"))
            try:
                parsed_date = datetime.strptime(item.job_status, "%d. %B")
                parsed_date = parsed_date.replace(year=datetime.now().year)
                fe.pubDate(
                    pytz.timezone(config.data.get("timezone")).localize(parsed_date)
                )
            except ValueError:
                fe.pubDate(
                    pytz.timezone(config.data.get("timezone")).localize(datetime.now())
                )
        self.fg.rss_str(pretty=True)
        self.fg.rss_file(output_file)
