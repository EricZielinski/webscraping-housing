import requests
from parsers.html_parser_factory import html_parser_factory


class BrokerData:

    def __init__(self, broker):
        self.broker = broker
        self.base_url = broker["base_url"]
        self.all_listings_url = broker["listings_url"]
        self.all_listings_page = requests.get(self.all_listings_url)
        self.parser = html_parser_factory("BeautifulSoup", self.all_listings_page.content)
        self.filter_fields = broker["filter"]
        self.url_truncator = broker["url_truncator"]
        self.link_to_each_listing = self.parser.get_links(self.filter_fields, self.base_url)
        if self.url_truncator is not None:
            self.truncate_links()

    def get_links(self):
        return self.link_to_each_listing

    def truncate_links(self):
        self.link_to_each_listing = [link.split(self.url_truncator)[0] for link in self.link_to_each_listing]

    def __repr__(self):
        return f'BrokerData({self.broker})'

    def __str__(self):
        return f'{ [link for link in self.link_to_each_listing] }'

