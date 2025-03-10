import json
import os
class Ware:
    def __init__(self, name: str, 
                 prise: int, 
                 description: str, 
                 imageURL: str):
        self.name = name
        self.price = prise
        self.description = description
        self.imageURL = imageURL
        self.id = id

        @classmethod
        def from_dick(cls, data: dict, id: int):
            return Ware(name=data['name'],
                        prise=data['prise'],
                        description=data['description'],
                        imageURL=data['imageURL'],
                        id=id)

    def get_ware_details(self):
        return f"{self.name}\nЦена: {self.price} руб.\n{self.description}\n"

    @classmethod
    def get_ware_by_id(cls, wares: list, id: int):
        for ware in wares:
            if ware.id == id:
                return ware

path = os.path.dirname(__file__)
path = os.path.join(path, 'wares.json')

with open('wares.json', 'r') as f:
    wares = json.load(f)
    wares = [Ware.from_dict(ware, id=index) for index, ware in enumerate(wares)]