from abc import abstractmethod, ABC
import json
import pickle


class SerializationInterface(ABC):
    @abstractmethod
    def get_data(self, unpacked_data):
        """

        :param unpacked_data:
        """
        pass

    @abstractmethod
    def save_data(self, some_data):
        """

        :param some_data:
        """
        pass


class PickleSInterface(SerializationInterface):
    def __init__(self, some_data, file_name):
        self.some_data = some_data
        self.file_name = file_name

    def save_data(self):
        with open(self.file_name, "wb") as fh:
            pickle.dump(self.some_data, fh)

    def get_data(self):
        with open(self.file_name, "rb") as fh:
            unpacked_data = pickle.load(fh)
        return unpacked_data


class JsonSInterface(SerializationInterface):
    def __init__(self, some_data, file_name):
        self.some_data = some_data
        self.file_name = file_name

    def save_data(self):
        with open(self.file_name, "wb") as fh:
            json.dump(self.some_data, fh)

    def get_data(self):
        with open(self.file_name, "rb") as fh:
            unpacked_data = json.load(fh)
        return unpacked_data

