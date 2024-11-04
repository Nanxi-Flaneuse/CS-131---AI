class package():
    # ind: unique id of the pacakge
    # w: weight of the package
    # v: value of the package
    def __init__(self, ind, w, v) -> None:
        self.index = ind
        self.weight = w
        self.value = v

    def get_weight(self):
        return self.weight
    
    def get_value(self):
        return self.value
    
    def get_index(self):
        return self.index
    
    def get_package(self):
        return (self.index, self.weight, self.value)