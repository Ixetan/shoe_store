class Address:
    def __init__(self, label, addresses):
        self.label = label
        self.address = addresses

    def to_dict(self):
        return dict(label=self.label, addressess=self)
    

    @classmethod
    def from_dict(cls, config):
        return Address(label=config['label'],
                            addresses=config['address'])