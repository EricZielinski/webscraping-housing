import requests
from parsers.html_parser_factory import html_parser_factory


class Listing:

    def __init__(self, url):
        self.data = \
            {
                'address': None, 'city': None, 'postcode': None, 'rent': None,
                'availability': None, 'size': None, 'rooms': None,
                'bathrooms': None, 'shared': False, 'url': url
            }

        self.get_offer_info(url)

    def to_dict(self):
        return self.data

    def __repr__(self):
        return f'Listing({self.data["url"]})'

    def __str__(self):
        return f'{ {key : value for key, value in self.data.items()} }'

    #refactor
    def get_offer_info(self, url):
        page = requests.get(url)
        parser = html_parser_factory("BeautifulSoup", page.content)

        address_container = parser.find(class_="container head")
        full_address = address_container.h1.contents[0].strip().split(",")
        self.data['address'] = full_address[0].strip(" ")
        self.data['postcode'] = " ".join(full_address[1].strip(" ").split(" ")[:2])
        self.data['city'] = full_address[1].strip(" ").split(" ")[-1]

        property_translations = {"rent": "Huurprijs", "size": "Totale woonoppervlakte", "rooms": "Slaapkamers", "bathrooms": "Badkamers"}

        properties = [prop.text.strip(":") for prop in parser.find_all(class_="kenmerklabel")]
        property_values = [value.text for value in parser.find_all(class_="kenmerk")]
        result = dict(zip(properties, property_values))

        for key in property_translations:
            if property_translations[key] in result:
                self.data[key] = result[property_translations[key]]


