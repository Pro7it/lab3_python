from abc import ABC


class BaseRepository(ABC):
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return list(self.model.objects.all())

    def get_by_id(self, _id):
        try:
            return self.model.objects.get(pk=_id)
        except Exception:
            return None

    def create(self, **kwargs):
        try:
            e = self.model(**kwargs)
            e.save()
            return e
        except Exception:
            return None
