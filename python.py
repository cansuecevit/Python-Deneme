__author_="Cansu ECEVİT"

while True:
    print("---------------------------------")
    isim = input("İsminiz:")
    print("Lütfen yemek istediğiniz kategoriyi seçiniz.")
    print("Fastfood ise(f) tatlı ise(t) basınız.")
    print("---------------------------------")
    print
    secim1=input()
    if secim1=="f":
        print("Lütfen fiyat bilgisini görmek için istediğiniz menüyü seçiniz.")
        print("Hamburger-kola (1)")
        print("Döner-ayran (2)")
        print("Pizza-gazoz (3)")
        secim2=int(input())
        if secim2==1:
            print("13 TL")
        elif secim2==2:
            print("11 Tl")
        elif secim2==3:
            print("14 Tl")
        else:
            print("Geçersiz tuşlama yaptınız.Program kapatılıyor.")
            break
    elif secim1=="t":
        print("Lütfen fiyat bilgisini görmek için istediğiniz menüyü seçiniz.")
        print("Waffle-çay (1)")
        print("Profiterol-kola (2)")
        secim2=int(input())
        if secim2==1:
            print("11 Tl")
        elif secim2==2:
            print("12 TL")
        else:
            print("Geçersiz tuşlama yaptınız.Program kapatılıyor.")
            break
    else:
        print("Geçersiz tuşlama yaptınız.Program kapatılıyor.")
        break
