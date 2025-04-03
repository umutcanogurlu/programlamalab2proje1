from karakter import Karakter

class DarthVader(Karakter):
    def __init__(self, ad, tur, konum):
        super().__init__(ad, tur, konum)

    def enKisaYol(self, harita, hedef):
        # Tüm duvarları kaldırarak en kısa yolu hesaplama algoritması
        duvarsiz_harita = [[0 if hucre == 1 else hucre for hucre in satir] for satir in harita]
        return super().enKisaYol(duvarsiz_harita, hedef)