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
        return f"No: {self.kayitNo} | Başlık: {self.baslik} | Yazar: {self.yazar} | Sayfa: {self.sayfa_sayisi} | Tür: {self.tur}"


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
        return f"No: {self.kayitNo} | Başlık: {self.baslik} | Yazar/Editör: {self.yazar} | Sayfa: {self.sayfa_sayisi} | Dönem: {self.yayin_donemi} | Sayı: {self.sayi_no}"

class Islem(ABC):
    @abstractmethod
    def ekle(self, nesne):
        pass

    @abstractmethod
    def sil(self, kayitNo: str):
        pass

    @abstractmethod
    def guncelle(self, kayitNo: str):
        pass

    @abstractmethod
    def listele(self):
        pass


class KitapIslem(Islem):
    def __init__(self):
        self.kitaplar = []

    def ekle(self, kitap: Kitap):
        for k in self.kitaplar:
            if k.kayitNo == kitap.kayitNo:
                print(f"Hata: {kitap.kayitNo} kayıt numaralı kitap zaten sistemde mevcut!")
                return False

        self.kitaplar.append(kitap)
        print("Kitap başarıyla eklendi.")
        print(f"Toplam Kitap Sayısı: {len(self.kitaplar)}")
        return True

    def sil(self, kayitNo: str):
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                self.kitaplar.remove(kitap)
                print(f"{kayitNo} numaralı kitap silindi.")
                return True
        print("Hata: Bu kayıt numarasına ait kitap bulunamadı.")
        return False

    def guncelle(self, kayitNo: str):
        for kitap in self.kitaplar:
            if kitap.kayitNo == kayitNo:
                print(f"Güncellenen Kitap: [{kitap.kayitNo}] {kitap.baslik}")

                yeni_baslik = input("Yeni Başlık: ")
                if yeni_baslik: kitap.baslik = yeni_baslik

                yeni_sayfa = input("Yeni Sayfa Sayısı: ")
                if yeni_sayfa: kitap.sayfa_sayisi = int(yeni_sayfa)

                yeni_yazar = input("Yeni Yazar: ")
                if yeni_yazar: kitap.yazar = yeni_yazar

                yeni_tur = input("Yeni Tür: ")
                if yeni_tur: kitap.tur = yeni_tur

                print("Kitap bilgileri güncellendi.")
                return True
        print("Hata: Kitap bulunamadı.")
        return False

    def listele(self):
        if not self.kitaplar:
            print("Kayıt bulunamadı.")
            return

        print("\n--- Kitap Listesi ---")
        for kitap in self.kitaplar:
            print(kitap)


class DergiIslem(Islem):
    def __init__(self):
        self.dergiler = []

    def ekle(self, dergi: Dergi):
        for d in self.dergiler:
            if d.kayitNo == dergi.kayitNo:
                print(f"Hata: {dergi.kayitNo} kayıt numaralı dergi zaten sistemde mevcut!")
                return False

        self.dergiler.append(dergi)
        print("Dergi başarıyla eklendi.")
        print(f"Toplam Dergi Sayısı: {len(self.dergiler)}")
        return True

    def sil(self, kayitNo: str):
        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                self.dergiler.remove(dergi)
                print(f"{kayitNo} numaralı dergi silindi.")
                return True
        print("Hata: Bu kayıt numarasına ait dergi bulunamadı.")
        return False

    def guncelle(self, kayitNo: str):
        for dergi in self.dergiler:
            if dergi.kayitNo == kayitNo:
                print(f"Güncellenen Dergi: [{dergi.kayitNo}] {dergi.baslik}")

                yeni_baslik = input("Yeni Başlık: ")
                if yeni_baslik: dergi.baslik = yeni_baslik

                yeni_sayfa = input("Yeni Sayfa Sayısı: ")
                if yeni_sayfa: dergi.sayfa_sayisi = int(yeni_sayfa)

                yeni_yazar = input("Yeni Yazar/Editör: ")
                if yeni_yazar: dergi.yazar = yeni_yazar

                yeni_donem = input("Yeni Yayın Dönemi: ")
                if yeni_donem: dergi.yayin_donemi = yeni_donem

                yeni_sayi = input("Yeni Sayı No: ")
                if yeni_sayi: dergi.sayi_no = int(yeni_sayi)

                print("Dergi bilgileri güncellendi.")
                return True
        print("Hata: Dergi bulunamadı.")
        return False

    def listele(self):
        if not self.dergiler:
            print("Kayıt bulunamadı.")
            return

        print("\n--- DERGİ LİSTESİ ---")
        for dergi in self.dergiler:
            print(dergi)

