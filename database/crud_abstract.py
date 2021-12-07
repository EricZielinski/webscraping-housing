from abc import ABC, abstractmethod


class DB(ABC):

    def __init__(self, db_conn):
        self.db_conn = db_conn

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, data_filter):
        pass

    @abstractmethod
    def update(self, data_filter, data):
        pass

    @abstractmethod
    def delete(self, data_filter):
        pass

    @abstractmethod
    def count(self, data_filter):
        pass

    @abstractmethod
    def create_index(self, data_key):
        pass


