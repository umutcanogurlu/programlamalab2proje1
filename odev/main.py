import tkinter as tk
from lokasyon import Lokasyon
from karakter import Karakter
from darthvader import DarthVader
from kyloren import KyloRen
from stormtrooper import Stormtrooper
from masteryoda import MasterYoda
from lukeskywalker import LukeSkywalker

class Oyun:
    def __init__(self, master):
        self.master = master
        self.master.title("Labirent Oyunu")
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()
        self.harita, self.kotu_karakterler = self.harita_oku("Star wars harita.txt")
        self.iyi_karakter = None
        self.oyuncu_baslangic_noktasi = Lokasyon(5, 6)
        self.iyi_karakter_sec()
        self.oyun_baslat()

    def harita_oku(self, dosya_adi):
        harita = []
        kotu_karakterler = []
        with open(dosya_adi, "r") as dosya:
            for satir in dosya:
                if "Karakter" in satir:
                    karakter_bilgileri = satir.strip().split(",")
                    karakter_turu = karakter_bilgileri[0].split(":")[1]
                    karakter_kapi = karakter_bilgileri[1].split(":")[1]
                    konum = self.kapi_konum_bul(karakter_kapi)
                    if karakter_turu == "DarthVader":
                        kotu_karakterler.append(DarthVader(karakter_turu, "Kötü", konum))
                    elif karakter_turu == "KyloRen":
                        kotu_karakterler.append(KyloRen(karakter_turu, "Kötü", konum))
                    elif karakter_turu == "Stormtrooper":
                        kotu_karakterler.append(Stormtrooper(karakter_turu, "Kötü", konum))
                else:
                    harita.append(list(map(int, satir.strip().split())))
        return harita, kotu_karakterler

    def kapi_konum_bul(self, kapi):
        kapi_konumlari = {
            "A": Lokasyon(0, 0),
            "B": Lokasyon(0, 13),
            "C": Lokasyon(9, 0),
            "D": Lokasyon(9, 13)
        }
        return kapi_konumlari[kapi]

    def iyi_karakter_sec(self):
        secim = input("İyi karakterinizi seçin (1: Luke Skywalker, 2: Master Yoda): ")
        if secim == "1":
            self.iyi_karakter = LukeSkywalker("Luke Skywalker", "İyi", self.oyuncu_baslangic_noktasi, 3)
        elif secim == "2":
            self.iyi_karakter = MasterYoda("Master Yoda", "İyi", self.oyuncu_baslangic_noktasi, 6)
        else:
            print("Geçersiz seçim!")
            self.iyi_karakter_sec()

    def oyun_baslat(self):
        self.canvas.delete("all")
        self.harita_ciz()
        self.iyi_karakter_ciz()
        self.kotu_karakterleri_ciz()
        self.master.bind("<KeyPress>", self.hareket_et)
        self.master.mainloop()

    def harita_ciz(self):
        for i, satir in enumerate(self.harita):
            for j, hucre in enumerate(satir):
                if hucre == 1:
                    self.canvas.create_rectangle(j*30, i*30, j*30+30, i*30+30, fill="black")
                elif hucre == 0:
                    self.canvas.create_rectangle(j*30, i*30, j*30+30, i*30+30, fill="white")

    def iyi_karakter_ciz(self):
        self.canvas.create_rectangle(self.iyi_karakter.getKonum().getX()*30, self.iyi_karakter.getKonum().getY()*30,
                                     self.iyi_karakter.getKonum().getX()*30+30, self.iyi_karakter.getKonum().getY()*30+30, fill="yellow")

    def kotu_karakterleri_ciz(self):
        for kotu_karakter in self.kotu_karakterler:
            self.canvas.create_rectangle(kotu_karakter.getKonum().getX()*30, kotu_karakter.getKonum().getY()*30,
                                         kotu_karakter.getKonum().getX()*30+30, kotu_karakter.getKonum().getY()*30+30, fill="red")

    def hareket_et(self, event):
        if event.keysym == "Up":
            self.iyi_karakter.getKonum().setY(self.iyi_karakter.getKonum().getY() - 1)
        elif event.keysym == "Down":
            self.iyi_karakter.getKonum().setY(self.iyi_karakter.getKonum().getY() + 1)
        elif event.keysym == "Left":
            self.iyi_karakter.getKonum().setX(self.iyi_karakter.getKonum().getX() - 1)
        elif event.keysym == "Right":
            self.iyi_karakter.getKonum().setX(self.iyi_karakter.getKonum().getX() + 1)
        self.kotu_karakterler_hareket()
        self.oyun_baslat()

    def kotu_karakterler_hareket(self):
        for kotu_karakter in self.kotu_karakterler:
            hedef = self.iyi_karakter.getKonum()
            mesafe = kotu_karakter.enKisaYol(self.harita, hedef)
            if mesafe == 1:
                if isinstance(self.iyi_karakter, LukeSkywalker):
                    self.iyi_karakter.setCan(self.iyi_karakter.getCan() - 1)
                elif isinstance(self.iyi_karakter, MasterYoda):
                    self.iyi_karakter.setCan(self.iyi_karakter.getCan() - 0.5)
                if self.iyi_karakter.getCan() <= 0:
                    print("Game Over!")
                    self.master.quit()
            else:
                yonler = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in yonler:
                    nx, ny = kotu_karakter.getKonum().getX() + dx, kotu_karakter.getKonum().getY() + dy
                    if 0 <= nx < len(self.harita) and 0 <= ny < len(self.harita[0]) and self.harita[nx][ny] == 0:
                        yeni_mesafe = kotu_karakter.enKisaYol(self.harita, Lokasyon(nx, ny))
                        if yeni_mesafe < mesafe:
                            kotu_karakter.getKonum().setX(nx)
                            kotu_karakter.getKonum().setY(ny)
                            break

if __name__ == "__main__":
    root = tk.Tk()
    oyun = Oyun(root)