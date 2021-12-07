import logging
import json

from database.crud import HousingDataCollection
from scrapers.broker import BrokerData
from scrapers.listing import Listing

#refactor
if __name__ == '__main__':
    logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8', level=logging.DEBUG)
    logging.info('Scraper is starting')

    broker_listing_urls = []
    with open("brokers.json") as brokers_file:
        brokers = json.load(brokers_file)["brokers"]
        for i in range(len(brokers)):
            broker = BrokerData(brokers[i])
            broker_listing_urls = broker.get_links()

    listings_data = []
    for link in broker_listing_urls:
        listings_data.append(Listing(link).to_dict())

    available_housing = HousingDataCollection("Web_Scraping_Housing")
    available_housing.create(listings_data)
