# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 22:13:39 2022

@author: ummug
"""

def bolum_bilgi():
    print(" - yarışma bölümleri hakkında bilgi alma işlemleri - ")
    print(""" Yarışma toplam 4 kategoriden oluşmaktadır.
              Her bölümde 4 kategoriden soru bulunmaktadır.
              yarışma kategorileriniz: 
                  -	Matematik
                  -	Türkçe
                  -	Genel kültür 
                  -	Fen 
""")

def joker_bilgi():
    print(" - jokerlerin hakkında bilgi alma işlemleri - ")
    print(""" Yarışmada toplam 3 joker kullanma hakkınız vardır.\n
1.joker hakkınız: soruyu iki kere cevaplama hakkı\n
2.joker hakkınız: soru ile ilgili ipucu alma hakkı\n
3.joker hakkınız: soruyu profesöre sor hakkı\n
""")

def bolum_soru_bilgi():
    print(""" - yarışmadaki bölüm soruları hakkında bilgi alma -\n
              Yarışma bölümlerinde toplam 4 soru bulunmaktadır.""")
def kazanilan_para():
    print(" - yarışmadaki kazanılan para hakkında bilgi alma - ")
    print("""yarışmada 4 bölüm vardır:
              1. bölüm para miktarı: 5.000$\n
              2. bölüm para miktarı: 25.000$\n
              3. bölüm para miktarı: 125.000$\n
              4. bölüm para miktarı: 500.000$\n
                """)

print( """ 
      ------- KİM BİLMEK İSTER YARIŞMASI ------------ \n
       ....Kim Bilmek İster Yarışmasına HOŞ GELDİNİZ...\n
       Öncelikle sisteme kayıt bilgilerinizi giriniz:\n
       
      """)


def fonksiyon_sec(fonksiyon_adi):
    if fonksiyon_adi == "joker_bilgi":
        joker_bilgi()

    elif fonksiyon_adi == "bolum_bilgi":
        bolum_bilgi()

    elif fonksiyon_adi == "bolum_soru_bilgi":
        bolum_soru_bilgi()

    elif fonksiyon_adi == "kazanilan_para":
        kazanilan_para()

print( " -Login User:- ")
k_adi = "root"
parola = "security123"

while (True):
    kullanici_adi = input("User Name: ")
    sifre = input("Password: ")

    if kullanici_adi == k_adi and sifre == parola:
        print("Sisteme hoşgeldiniz.")
        break
    elif  ((k_adi != kullanici_adi) and (parola == sifre)):
     print("Kullanıcı Adı Hatalı Lütfen Tekrar Deneyiniz...")
    elif  ((k_adi == kullanici_adi) and (parola != sifre)):
      print("Şifreniz Hatalı Lütfen Tekrar Deneyiniz...")
    elif not k_adi.strip() and not parola.strip():
        print("Kullanıcı adı ve parola alanı boş bırakılamaz.")
    elif not k_adi.strip():
        print("Kullanıcı adı alanı boş bırakılmaz.")
    elif not parola.strip():
        print("Parola alanı boş bırakılmaz.")
    else:
        print("Hatalı parola ve kullanıcı adı.")

bilgi=input("Oyun ile ilgili ön bilgi almak için 1 yazın:\n")
if bilgi == "1":
    print("menüye yönlendiriliyorsunuz...")
    

seciminiz=""
    
fonksiyonListesi=["joker_bilgi","bolum_bilgi", "bolum_soru_bilgi", "kazanilan_para" ]


while True:
    print("1-Jokerlerin hakkında bilgi alma")
    print("2-Bölüm Bilgileri alma")
    print("3-Bölüm Soruları ile ilgili bilgi alma ")
    print("4-Bölümlerde kazanılan para ile ilgili bilgi alma")
    print("0-Programdan Çık")
                 
    seciminiz=int(input("Lütfen Yapmak İstediğiniz İşlem Seçiniz (0-4):"))
            
    if seciminiz<=4 and seciminiz>=1:
        secilen_fonksiyon = fonksiyonListesi[seciminiz-1]
        fonksiyon_sec(secilen_fonksiyon)

        print("\n" * 2)
        
    elif seciminiz==0:
        print("Çıkış Yapılıyor")
        break

    else:
        print("Lütfen Seçim İçin 0 ile 5 arası bir rakam giriniz!")

bolum1_sorular=["2003 Yılında Euro Vizyon Şarkı Yarışmasında Ülkemizi Temsil Eden ve Yarışmada Birinci Gelen Sanatçımız Kimdir?",
"Sancho Panza hangi romandaki yan karakterdir?", "Ornitoloji hangisini inceleyen bilim dalıdır?", "Bir Gün Kaç Saniyedir?"]

bolum2_sorular=["Hangisini onaran veya yapıp satan kişiye 'lutiye' denir?", "' David Fincher ve David Lynch' diyen birine muhtemelen hangisi sorulmuştur?",
"Cevabı 'sam yeli' olan bir bulmaca sorusunda sorulan hangisi olur?", "Matematikte hangi adda bir sayı grubu vardır?"]

bolum3_sorular=["Sherlock Holmes'un birçok macerasında yanında olan yakın dostu ve yardımcısı kimdir?", "Gabardin nedir?",
"Hangisinin eski adı 'amudufıkari'dir?", "1 milyon kere 1 milyon kaç eder?"]

bolum4_sorular=["Pürdikkat ne demektir?", "Ana taşıyıcı kuleleri arasındaki mesafe en uzun olan, 'en uzun asma köprü' hangisidir?",
"Fransa'dan trene binip deniz altındaki Manş Tüneli'nden geçen biri hangi ülkeye ulaşır?", "Üçün üç katından ikinin iki katı çıkarılırsa ne olur?"]

bolum1_soru1cevaplar=['A) Grup Athena', 'B) Sertap Erener', 'C) Şebnem Paker', 'D) Ajda Pekkan']
bolum1_soru2cevaplar=['A) Moby Dick',  'B) Don Kişot', 'C) Sefiller' 'D) Suç ve Ceza']
bolum1_soru3cevaplar=['A) Orangutanları', 'B) Orkinosları', 'C) Ornitorenkleri', 'D) Kuşları']
bolum1_soru4cevaplar=['A) 86000', 'B) 88600', 'C) 86400' , 'D) 84800']

bolum2_soru1cevaplar=['A) Beyaz eşya', 'B) Mobilya', 'C) Enstrüman', 'D) Oyuncak']
bolum2_soru2cevaplar=['A)En sevdiği iki ünlü futbolcu','B)En sevdiği iki ünlü şair','C) En sevdiği iki ünlü şair','D) En sevdiği iki ünlü tenisçi']
bolum2_soru3cevaplar=['A) Çölden esen sıcak rüzgar','B)Denizden esen soğuk rüzgar','C) Nehirden esen sıcak rüzgar', 'D) Dağdan esen soğuk rüzgar']
bolum2_soru4cevaplar=['A) Samimi sayılar', 'B) Dürüst sayılar', 'C) İçten sayılar', 'D) Doğal sayılar']

bolum3_soru1cevaplar=['A) Hercule Poirot', 'B) Dr. Watson', 'C) Müfettiş Clouseau', 'D) Miss Marple']
bolum3_soru2cevaplar=['A) Bir enstrüman çeşidi', 'B) Bir köpek cinsi', 'C) Bir kumaş türü', 'D) Bir saç modeli']
bolum3_soru3cevaplar=['A) Bel kemiği', 'B) Kaval kemiği', 'C) Kürek kemiği', 'D) Tarak kemiği']
bolum3_soru4cevaplar=['A) 2 milyon', 'B) 100 milyon', 'C) 1 milyar', 'D) 1 trilyon']

bolum4_soru1cevaplar=['A) Dikkatsizce', 'B) Çok dikkatli', 'C) Gelişigüzel', 'D) Lalettayin']
bolum4_soru1cevaplar=["A) Japonya'daki Akaşi Kaikyo Köprüsü", "B) Japonya'daki Akaşi Kaikyo Köprüsü", "C) Çin'deki Yangtze Köprüsü", "D) ABD'deki Golden Gate Köprüsü"]
bolum4_soru1cevaplar=['A) Birleşik Krallık', 'B) Almanya', 'C) İzlanda', 'D) Portekiz']
bolum4_soru1cevaplar=['A) 1', ' B) 2', 'C) 5', 'D) 2']

bolum1dogru_cevaplar = ['b','b','d','c']
bolum2dogru_cevaplar = ['c','a','c','d']
bolum3dogru_cevaplar = ['b','c','a','d']
bolum4dogru_cevaplar = ['b','b','a','c']

def sor():

    puan = 0

    print('Soru 1:',bolum1_sorular[0])

    for x in bolum1_soru1cevaplar:

        print(x)

    cevap_1 = input('Cevabınız Nedir: ')

    if (cevap_1.lower() == bolum1dogru_cevaplar[0]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap A Şıkkı.')

    print('-'*50)
    
    
    print('Soru 2:',bolum1_sorular[1])

    for x in bolum1_soru2cevaplar:

        print(x)

    cevap_2 = input('Cevabınız Nedir: ')

    if (cevap_2.lower() == bolum1dogru_cevaplar[1]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap A Şıkkı.')

    print('-'*50)
    
    print('Soru 3:',bolum1_sorular[2])

    for x in bolum1_soru3cevaplar:

        print(x)

    cevap_3 = input('Cevabınız Nedir: ')

    if (cevap_3.lower() == bolum1dogru_cevaplar[2]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap A Şıkkı.')

    print('-'*50)
    
    print('Soru 4:',bolum1_sorular[3])

    for x in bolum1_soru4cevaplar:

        print(x)

    cevap_4 = input('Cevabınız Nedir: ')

    if (cevap_4.lower() == bolum1dogru_cevaplar[3]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap A Şıkkı.')

    print('-'*50)
    
    print('Soru 5:',bolum1_sorular[3])

    for x in bolum1_soru4cevaplar:

        print(x)

    cevap_4 = input('Cevabınız Nedir: ')

    if (cevap_4.lower() == bolum1dogru_cevaplar[3]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap A Şıkkı.')

    print('-'*50)
    
    
    
    
    
    


    


