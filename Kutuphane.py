from abc import ABC, abstractmethod

class Kaynak(ABC):
    def __init__(self, kayitNo: str, baslik: str, sayfa_sayisi: int, yazar: str):
        self._kayitNo = kayitNo
        self._baslik = baslik
        self._sayfa_sayisi = sayfa_sayisi
        self._yazar = yazar
    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, value):
        self._kayitNo = value

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, value):
        self._sayfa_sayisi = value

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, value):
        self._yazar = value


class Kitap(Kaynak):
    def __init__(self, kayitNo: str, baslik: str, sayfa_sayisi: int, yazar: str, tur: str):
        super().__init__(kayitNo, baslik, sayfa_sayisi, yazar)
        self._tur = tur
    @property
    def tur(self):
        return self._tur

    @tur.setter
    def tur(self, value):
        self._tur = value

    def __str__(self):
        return f"[Kitap] No: {self.kayitNo} | Başlık: {self.baslik} | Yazar: {self.yazar} | Sayfa: {self.sayfa_sayisi} | Tür: {self.tur}"


class Dergi(Kaynak):
    def __init__(self, kayitNo: str, baslik: str, sayfa_sayisi: int, yazar: str, yayin_donemi: str, sayi_no: int):
        super().__init__(kayitNo, baslik, sayfa_sayisi, yazar)
        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no
    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, value):
        self._yayin_donemi = value

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, value):
        self._sayi_no = value

    def __str__(self):
        return f"[Dergi] No: {self.kayitNo} | Başlık: {self.baslik} | Yazar/Editör: {self.yazar} | Sayfa: {self.sayfa_sayisi} | Dönem: {self.yayin_donemi} | Sayı: {self.sayi_no}"

