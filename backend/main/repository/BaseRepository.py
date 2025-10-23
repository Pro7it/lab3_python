from abc import abstractmethod, ABC

class BaseRepository(ABC):
    def __init__(self, model):
        self.model = model

    def get_all(self):
        pass

    def get_by_id(self, id):
        pass

    def create(self, **kwargs):
        pass
