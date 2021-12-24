from bs4 import BeautifulSoup


class BS:

    def __init__(self, page):
        self.parsed_page = BeautifulSoup(page, "html.parser")

    def __get_data(self, bs_filter: str):
        return self.parsed_page.select(bs_filter)

    def get_urls(self, bs_filter: str, domain_name: str):
        listing_uris = self.__get_data(bs_filter)
        return [self.__create_url(uri, domain_name) for uri in listing_uris]

    def __create_url(self, uri: str, domain_name: str):
        return f'{domain_name}{uri.get("href")}'

    def get_address(self, bs_filter: str):
        return self.__get_data(bs_filter)[0].contents[0].strip().split(",")

    def get_properties(self, bs_filter: str):
        properties = self.__get_data(bs_filter)
        return [prop.text.strip(":") for prop in properties]
