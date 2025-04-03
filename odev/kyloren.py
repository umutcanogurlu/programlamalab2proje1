from karakter import Karakter

class KyloRen(Karakter):
    def __init__(self, ad, tur, konum):
        super().__init__(ad, tur, konum)

    def enKisaYol(self, harita, hedef):
        # Tek harekette iki birim birden gidecek şekilde en kısa yolu hesaplama algoritması
        satir_sayisi = len(harita)
        sutun_sayisi = len(harita[0])
        mesafe = [[float('inf')] * sutun_sayisi for _ in range(satir_sayisi)]
        mesafe[self.konum.getX()][self.konum.getY()] = 0
        pq = [(0, self.konum.getX(), self.konum.getY())]
        yonler = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        while pq:
            mevcut_mesafe, x, y = heapq.heappop(pq)
            if (x, y) == (hedef.getX(), hedef.getY()):
                break
            for dx, dy in yonler:
                nx, ny = x + dx, y + dy
                if 0 <= nx < satir_sayisi and 0 <= ny < sutun_sayisi and harita[nx][ny] == 0:
                    yeni_mesafe = mevcut_mesafe + 1
                    if yeni_mesafe < mesafe[nx][ny]:
                        mesafe[nx][ny] = yeni_mesafe
                        heapq.heappush(pq, (yeni_mesafe, nx, ny))

        return mesafe[hedef.getX()][hedef.getY()]