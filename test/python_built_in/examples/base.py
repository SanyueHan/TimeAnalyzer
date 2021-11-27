

class ComparatorBase:
    def __init__(self, limit):
        self.limit = limit

    def run(self):
        for name, value in self.__class__.__dict__.items():
            if name.startswith("method"):
                value(self)
