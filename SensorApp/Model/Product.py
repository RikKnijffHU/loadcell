class Product(object):
    
    def __init__(self, name, weight, DT, SCK, container):
        self.name = name
        self.weight = weight
        self.DT = DT
        self.SCK = SCK
        self.container = container
        self.amount = 0
