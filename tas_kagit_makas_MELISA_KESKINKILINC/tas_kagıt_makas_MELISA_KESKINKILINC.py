import random
def tas_kagıt_makas_MELISA_KESKINKILINC():
    print("\nTaş kağıt makas oyununa hoş geldiniz!!!")
    print("Oyun kuralları şu şekildedir: ","\nKağıt taşı sarar. Makas kağıdı keser.Taş makası kırar.","\nHer oyun üç turdan oluşmaktadır.Üç tur sonucunda önde tamamlayan taraf oyunun galibi olur."," \nToplamda 5 tur yenen şampiyon olur.")
    print("Bol şans!!!🍀")
    
    def oyun_skor(bilgisayar_secim, oyuncu_secim, bilgisayar_skor, oyuncu_skor):
            if(bilgisayar_secim == "TAŞ" and oyuncu_secim =="TAŞ" ):
                print (" BERABERE!🤜🤛")
        
            elif (bilgisayar_secim == "TAŞ" and oyuncu_secim =="MAKAS" ):
                print(" Bilgisayar Kazandı!💻")
                print("Skor")
                bilgisayar_skor += 1
        
            elif (bilgisayar_secim == "TAŞ" and oyuncu_secim =="KAĞIT" ):
                print("TEBRİKLER!🎉") 
                oyuncu_skor += 1        
        
            elif (bilgisayar_secim == "KAĞIT" and oyuncu_secim =="MAKAS" ):
                print("TEBRİKLER!🎉")
                oyuncu_skor += 1
        
            elif (bilgisayar_secim == "KAĞIT" and oyuncu_secim =="TAŞ" ):
                print("Bilgisayar kazandı!💻")
                bilgisayar_skor += 1
        
            elif (bilgisayar_secim == "KAĞIT" and oyuncu_secim =="KAĞIT" ):
                print("BERABERE!🤜🤛")
                
            elif (bilgisayar_secim == "MAKAS" and oyuncu_secim =="KAĞIT" ):
                print("Bilgisayar Kazandı!💻")  
                bilgisayar_skor +=1
        
            elif (bilgisayar_secim == "MAKAS" and oyuncu_secim =="TAŞ" ):
                print("TEBRİKLER!🎉")
                oyuncu_skor +=1
    
            elif (bilgisayar_secim == "MAKAS" and oyuncu_secim =="MAKAS" ):
                print("BERABERE!🤜🤛") 
        
            print("📊 Bilgisayar:",bilgisayar_skor,"-",oyuncu_skor,":Oyuncu")
            return bilgisayar_skor,oyuncu_skor

    def oyun_döngüsü():
        toplam_bilgisayar_skor = 0
        toplam_oyuncu_skor = 0
        oyun = 0

        while toplam_bilgisayar_skor < 5 and toplam_oyuncu_skor < 5:
            bilgisayar_skor = 0
            oyuncu_skor = 0
            oyun += 1
            tur = 0
            while tur < 3 :
                tur += 1
                print(f"\nOyun:{oyun}",f"Tur: {tur}")
                print("Seçim yapınız: TAŞ, KAĞIT, MAKAS, ÇIKIŞ")
                oyuncu_secim = input().strip().upper()
                if oyuncu_secim == "ÇIKIŞ":
                    print("Oyundan çıkış yapıldı.👋")
                    return
            
                secenekler = ["TAŞ", "KAĞIT", "MAKAS"]
                if oyuncu_secim not in secenekler:
                    print("Geçersiz seçim yaptınız.")
                    continue
            
                bilgisayar_secim = random.choice(secenekler)
                print("Bilgisayarın seçimi:", bilgisayar_secim)
            
                bilgisayar_skor, oyuncu_skor = oyun_skor(bilgisayar_secim, oyuncu_secim, bilgisayar_skor, oyuncu_skor)

            if bilgisayar_skor >oyuncu_skor:
                print("Oyunun Galibi Bilgisayar Oldu!💻")
                toplam_bilgisayar_skor += 1
                
            elif oyuncu_skor >bilgisayar_skor:
                print("TEBRİKLER! Oyunun Galibi Oldunuz!🥇")
                toplam_oyuncu_skor += 1
                
            elif oyuncu_skor == bilgisayar_skor:
                print("Oyun Berabere Sonuçlandı!🤝")
            
                
            if tur % 3 == 0 and  random.choice([True, False])<0.05:
                print("\nBilgisayar oyundan çekildi...🏳️\n")
                return

            print(f"\nToplam Skor - Bilgisayar: {toplam_bilgisayar_skor} 🆚 Oyuncu: {toplam_oyuncu_skor}")
        
        if toplam_bilgisayar_skor >= 5:
            print("Bilgisayar Şampiyon Oldu!")
            print("🦾")
            
        elif toplam_oyuncu_skor >= 5:
            print("TEBRİKLER! Şampiyon Oldunuz!🥳")
            print("🏆")
            
    oyun_döngüsü()
    
tas_kagıt_makas_MELISA_KESKINKILINC()
