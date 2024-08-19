# TAŞ KAĞIT MAKAS OYUNU
Bu proje Aygaz Python Bootcamp: Yeni Nesil Proje Kampı kapsamında hazırlanmıştır.
Bilgisayara karşı oynanan bu oyunda, her oyun 3 turdan oluşmakta ve 3 tur sonucunda önde tamamlayan taraf oyunun galibi olmaktadır. Ayrıca 5 tur kazanan taraf şampiyon olmaktadır.
Bilgisayarın seçenekler içerisinden rastgele seçim yapabilmesi için random kütüphanesi kullanılmıştır. Ayrıca hem bilgisayar hem de oyuncu istediği an oyundan çıkış yapabilme hakkına sahiptir. Ancak bilgisayarın rastgele çıkış yapma ihtimalini azaltmak için her 3 tur sonunda çıkış yapma ihtimali %5'den az olacak şekilde ayarlanmıştır. 

Klavyeden girilecek girdinin büyük-küçük harf hassasiyetini engellemek için .upper() metodu, oyuncu yanlışlıkla boşluk bırakırsa hatalı girişi engellemek için .strip() metodu kullanılmıştır.
oyun_skor fonksiyonu içerisinde bilgisayar ve kullanıcı girişlerinin kıyaslanması if elif yapıları ile sağlanmış ve kazanan tarafın skor artışı sağlanmıştır. oyun_döngüsü fonksiyonu içerisinde oyunun galibinin ve şampiyonun belirlenmesi için toplam skor hesaplanmıştır. While döngüleri içerisinde if elif yapıları kullanılmıştır. Oyun akıcılığını sağlamak ve görselleştirme amacıyla galibiyet, mağlubiyet ve beraberlik gibi durumlar emojilerle görselleştirilmiştir. Python halihazırda emoji kullanımını desteklediği için ek bir kütüphane kullanılmamıştır.

## Oyun Kuralları
Kullanıcı taş kağıt ve makas seçeneklerinden birini seçmelidir. Kağıt taşı sarar,makas kağıdı keser,taş makası kırar. Örneğin kullanıcı taş seçmesi durumunda bilgisayar makası seçerse kullanıcı kazanır. Ancak bilgisayar kağıdı seçerse bilgisayar kazanır. Bilgisayarın taşı seçmesi durumunda berabere sonuçlanır. Her oyun 3 turdan oluşmakta ve 3 tur sonucunda önde tamamlayan taraf oyunun galibi olmaktadır. Ayrıca 5 tur kazanan taraf şampiyon olmaktadır. Kullanıcı yanlış giriş yaptığında "Hatalı eçim yaptınız." uyarısı alır. Eğer hatalı giriş yapılırsa o tur geçerli sayılır ancak kazananı olmayacaktır. Kullanıcı ve bilgisayar istediği an oyundan çıkış yapma hakkına sahiptir.Çıkış seçeneğini seçerek oyundan çıkış yapabilir.

## Geliştirme Tavsiyeleri
Bilgisayarın çıkış yapma ihtimali arttırılıp azaltılabilir.
Hatalı giriş yapıldığında kullanıcıdan tekrar geçerli giriş istenebilir.

## Kullanılan Program ve Sürümler
Kodlar Visual Studio Code ortamında,
Python version 3.7.6 
anaconda version 1.7.2 
kullanılarak hazırlanmıştır.
Oyunu oynayabilmek için kodları çalıştırıp terminal ekranından oyunu oynayabilirsiniz.
