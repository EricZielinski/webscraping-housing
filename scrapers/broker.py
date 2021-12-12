from scrapers.url import URLScraper
from scrapers.listing import ListingScraper


class BrokerListings:

    def __init__(self, broker, parser):
        self.broker = broker
        url_to_each_listing = URLScraper(broker, parser).get_urls()
        self.listings = [Listing(broker, parser, url).get_listing() for url in url_to_each_listing]

    def get_listings(self):
        return self.listings

    def __repr__(self):
        return f'BrokerData({self.broker})'

    def __str__(self):
        return f'{ [listing for listing in self.listings] }'


class Listing:

    def __init__(self, broker, parser, url):
        self.property_translations = broker.get("property_translations", None)
        self.listing = \
            {
                'street': None, 'city': None, 'postcode': None, 'rent': None,
                'availability': None, 'size': None, 'rooms': None,
                'bathrooms': None, 'shared': False, 'url': url
            }
        raw_data = ListingScraper(broker, parser, url).get_listing()
        self.__populate_listing(raw_data)

    def get_listing(self):
        return self.listing

    def __populate_listing(self, raw_data):
        for key in self.property_translations:
            if self.property_translations[key] in raw_data:
                self.listing[key] = raw_data[self.property_translations[key]]
        for key in self.listing:
            if key in raw_data:
                self.listing[key] = raw_data[key]

    def __repr__(self):
        return f'Listing({self.listing["url"]})'

    def __str__(self):
        return f'{ {key : value for key, value in self.listing.items()} }'

