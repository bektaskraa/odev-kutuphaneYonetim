from Kutuphane import *
class Menu:
    def __init__(self):
        self.kitap_islem = KitapIslem()
        self.dergi_islem = DergiIslem()

    def menu(self):
        print("\n" + "=" * 35)
        print(" KÜTÜPHANE YÖNETİM SİSTEMİ")
        print("=" * 35)
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Güncelle")
        print("4. Kitapları Listele")
        print("5. Dergi Ekle")
        print("6. Dergi Sil")
        print("7. Dergi Güncelle")
        print("8. Dergileri Listele")
        print("9. Çıkış")
        print("=" * 35)

    def calistir(self):
        while True:
            self.menu()
            secim = input("Yapmak istediğiniz işlemi seçin (1-9): ")

            if secim == "1":
                kayit_no = input("Kitabın kayıt numarasını girin: ")
                baslik = input("Kitabın başlığını girin: ")
                sayfa = int(input("Kitabın sayfa sayısını girin: "))
                yazar = input("Kitabın yazarını girin: ")
                tur = input("Kitabın türünü girin: ")
                yeni_kitap = Kitap(kayit_no, baslik, sayfa, yazar, tur)
                self.kitap_islem.ekle(yeni_kitap)

            elif secim == "2":
                kayit_no = input("Silinecek kitabın kayıt numarasını girin: ")
                self.kitap_islem.sil(kayit_no)

            elif secim == "3":
                kayit_no = input("Güncellenecek kitabın kayıt numarasını girin: ")
                self.kitap_islem.guncelle(kayit_no)

            elif secim == "4":
                self.kitap_islem.listele()

            elif secim == "5":
                kayit_no = input("Derginin kayıt numarasını girin: ")
                baslik = input("Derginin başlığını girin: ")
                sayfa = int(input("Derginin sayfa sayısını girin: "))
                yazar = input("Derginin yazarını/editörünü girin: ")
                donem = input("Derginin yayın dönemini girin (Aylık vs.): ")
                sayi_no = int(input("Derginin sayı numarasını girin: "))
                yeni_dergi = Dergi(kayit_no, baslik, sayfa, yazar, donem, sayi_no)
                self.dergi_islem.ekle(yeni_dergi)

            elif secim == "6":
                kayit_no = input("Silinecek derginin kayıt numarasını girin: ")
                self.dergi_islem.sil(kayit_no)

            elif secim == "7":
                kayit_no = input("Güncellenecek derginin kayıt numarasını girin: ")
                self.dergi_islem.guncelle(kayit_no)

            elif secim == "8":
                self.dergi_islem.listele()

            elif secim == "9":
                print("Kapatılıyor...")
                break

            else:
                print("Geçersiz seçim! Sadece 1 ile 9 arasında bir sayı girin.")

if __name__ == "__main__":
    uygulama = Menu()
    uygulama.calistir()