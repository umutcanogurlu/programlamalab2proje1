from karakter import Karakter

class MasterYoda(Karakter):
    def __init__(self, ad, tur, konum, can):
        super().__init__(ad, tur, konum)
        self.can = can

    def getCan(self):
        return self.can

    def setCan(self, can):
        self.can = can