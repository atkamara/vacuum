from .Model import Item
from datetime import datetime

class MainItem(Item):
    def __post_init__(self):
        for field in self.registry:
            self.__setattr__(field,field.get_value())
        self.created_at = datetime.now()