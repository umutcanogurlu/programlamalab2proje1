from karakter import Karakter

class Stormtrooper(Karakter):
    def __init__(self, ad, tur, konum):
        super().__init__(ad, tur, konum)

    def enKisaYol(self, harita, hedef):
        return super().enKisaYol(harita, hedef)