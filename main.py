import logging
import json

from scrapers.broker import BrokerListings
from utilities.config import JSONConfig

#refactor
if __name__ == '__main__':
    logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8', level=logging.DEBUG)
    logging.info('Scraper is starting')

    parser = "BeautifulSoup"

    all_listings_data = []
    with open("brokers.json") as brokers_file:
        brokers = json.load(brokers_file)["brokers"]

        logging.info('Checking broker configuration file')
        JSONConfig("brokers", brokers).check()

        logging.info('Getting listings data from brokers')
        for i in range(len(brokers)):
            broker = BrokerListings(brokers[i], parser)
            all_listings_data.append(broker.get_listings())

    flattened_data = [offer for broker_offers in all_listings_data for offer in broker_offers]
    print(flattened_data)
    # listings_data = []
    # for link in broker_listing_urls:
    #     listings_data.append(Listing(link, parser).to_dict())
    #
    # print(listings_data)
    # available_housing = Collection("Web_Scraping_Housing")
    # available_housing.create(listings_data)
