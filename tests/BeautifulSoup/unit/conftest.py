import pytest


@pytest.fixture()
def config():
    config = {
              "brokers":
                [
                  {
                    "domain_name": "a",
                    "listings_url": "b",
                    "url_delineator": "b",
                    "url_filter": "d",
                    "address_filter": "e",
                    "property_filters": {
                      "property_key_filter": "f",
                      "property_value_filter": "g"
                    },
                    "property_translations": {
                      "rent": "h",
                    }
                  }
                ]
              }
    return config


