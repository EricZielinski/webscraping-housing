import pymongo
from database.crud_abstract import DB
from utilities.yaml_methods import get_mongodb_config


class MongoDB(DB):

    def __init__(self):
        self.db_conn = pymongo.MongoClient(get_mongodb_config())

    def create(self, data):
        pass

    def read(self, data_filter):
        pass

    def update(self, data_filter, data):
        pass

    def delete(self, data_filter):
        pass

    def count(self, data_filter):
        pass

    def create_index(self, data_key):
        pass


class Collection(MongoDB):

    def __init__(self, collection):
        super().__init__()
        self.collection = self.db_conn[f'{collection}']

    def create(self, data={}):
        self.collection.Collection.insert_one(data)

    def create(self, data=[]):
        self.collection.Collection.insert_many(data)

    def read(self, data_filter):
        self.collection.Collection.find(data_filter)

    def update(self, data_filter, data={}):
        self.collection.Collection.update_one(data_filter, data)

    def update(self, data_filter, data=[]):
        self.collection.Collection.update_many(data_filter, data)

    def delete(self, data_filter={}):
        self.collection.Collection.delete_one(data_filter)

    def delete(self, data_filter=[]):
        self.collection.Collection.delete_many(data_filter)

    def count(self, data_filter):
        return self.collection.Collection.count_documents(data_filter)

    def create_index(self, data_key):
        self.collection.Collection.create_index(data_key)





