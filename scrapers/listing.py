import requests
from parsers.html_parser_factory import html_parser_factory


class ListingScraper:
    def __init__(self, broker, parser, listing_url):
        self.address_filter = broker.get("address_filter", None)
        self.property_filter = broker.get("property_filters", None)
        self.parser = parser
        self.listing_url = listing_url

    def get_listing(self):
        page = requests.get(self.listing_url)
        listing_page = html_parser_factory(self.parser, page.content)
        listing = self.__get_props(listing_page)

        if self.address_filter is not None:
            address = self.__get_address(listing_page)
            listing.update(address)

        return listing

    def __get_address(self, listing_page):
        address_container = listing_page.get_address(self.address_filter)
        address = {"street": address_container[0].strip(" "),
                   "postcode": " ".join(address_container[1].strip(" ").split(" ")[:2]),
                   "city": address_container[1].strip(" ").split(" ")[-1]
                   }

        return address

    def __get_props(self, listing_page):
        property_keys = listing_page.get_properties(self.property_filter["property_key_filter"])
        property_values = listing_page.get_properties(self.property_filter["property_value_filter"])

        listing = dict(zip(property_keys, property_values))

        return listing
