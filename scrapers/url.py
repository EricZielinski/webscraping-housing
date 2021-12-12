import requests
from parsers.html_parser_factory import html_parser_factory


class URLScraper:
    def __init__(self, broker, parser):
        self.domain_name = broker["domain_name"]
        self.all_listings_url = broker["listings_url"]
        self.filter = broker["url_filter"]
        self.url_delineator = broker["url_delineator"]
        self.parser = parser

    def get_urls(self):
        all_listings_page = requests.get(self.all_listings_url)
        all_listings_page_parsed = html_parser_factory(self.parser, all_listings_page.content)
        url_to_each_listing = all_listings_page_parsed.get_urls(self.filter, self.domain_name)
        if self.url_delineator is not None:
            url_to_each_listing = self.__truncate_urls(url_to_each_listing)

        return url_to_each_listing

    def __truncate_urls(self, url_to_each_listing):
        return [url.split(self.url_delineator)[0] for url in url_to_each_listing]


