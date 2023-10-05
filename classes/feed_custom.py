from classes.feed import Feed


class FeedCustom(Feed):
    def __init__(self, feed_id, feed_title, feed_subtitle, feed_link_href, data, output_file):
        super().__init__(feed_id, feed_title, feed_subtitle, feed_link_href)
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
        self.fg.rss_str(pretty=True)
        self.fg.rss_file(output_file)
