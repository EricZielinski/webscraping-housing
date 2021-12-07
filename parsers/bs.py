from bs4 import BeautifulSoup


class BS:

    def __init__(self, page, parser):
        self.parsed_page = BeautifulSoup(page, parser)

    def get_links(self, filter_fields, base_url):
        offer_links = []
        for offer in self.parsed_page.find_all(
                filter_fields["identifier"], filter_fields["identifier_name"]):
            offer_links.append(f'{base_url}{offer.get("href")}')
        return offer_links
