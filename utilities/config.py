class JSONConfig:
    def __init__(self, parent, config):
        self.config = config[parent]
        self.fields = [
            "domain_name",
            "listings_url",
            "url_delineator",
            "url_filter",
            "address_filter",
            "property_filters",
            "property_translations"
            ]
        self.subfields = [("property_translations", 1), ("property_filters", 2)]

    def check(self):
        self.__check_count()
        self.__check_fields()

    def __check_fields(self):
        for broker in self.config:
            for field in self.fields:
                if field not in broker.keys():
                    raise Exception(f"Missing field '{field}' in config")
            self.__check_subfields(broker)

    def __check_subfields(self, broker):
        for field in self.subfields:
            if len(broker.get(field[0]).keys()) < field[1]:
                raise Exception(f"Missing subfield(s) under '{field[0]}' in config")

    def __check_count(self):
        if len(self.config) < 1:
            raise Exception("No brokers found in json file")

