# Data Science SQL Project - THE BASICS

### Proje Kurulumu
Projeyi öncelikle forklayın ve clone edin.
Proje sayımız ilerledikçe proje yönetimimizi kolaylaştırmak adına projelerimizi belli klasör kalıplarında saklamak işimizi kolaylaştırmak adına iyi bir alışkanlıktır.
Örnek bir Lokasyon: Code2Work/DataScience/data-projects

### Proje Kurulumu Komutlar
Aşağıdaki komutları sıtrayla çalıştırınız.
* python -m venv venv
* venv\Scripts\activate - source venv/bin/activate
* pip install -r requirements.txt => Install all dependencies
* python watch.py => Python run all tests

## Bonus
* Eğer daha detaylı bir şekilde testlerin içerisine bakmak isterseniz
* pytest .\tests\test_question.py -s -v 

### Projeye Başlamadan Önce
* Belirtilen sql querylerini yazabilmek için scripts klasörü altındaki bulunan init_db.py dosyası içerisindeki tüm queryleri 
sırasıyla kendi local veritabanınızda çalıştırınız. 
* Veritabanınızın hazır olduğundan emin olmak için tüm tablolara birer SELECT sorgusu atıp sonuçların doğru olduğundan emin olunuz.
* Çalışırken sadece data klasörü altında bulunan questions.py dosyasında çalışacağız. Bunun klasör dışındaki kodları değiştirmeyiniz !
* connect_db fonksiyonu içerisinde veritabanına bağlanma bilgileri var. Projenizi kendi localinizde test ederken burada bilgileri kendi local veritabanı bilgilerinizle değiştirerek test ediniz. Ancak kodunuzu <b>pushlarken bu veritabanı bilgilerini ilk bulduğunuz şekilde bırakınız.</b> Çünkü kodlarınız Cloud bir ortamda bu bilgilerle bir veritabanına bağlancaklardır.

# Questions
1. customers tablosundan tüm müşterilerin adlarını ve ülkelerini getir.
2. orders tablosunda en yüksek tutarlı 5 siparişi listele (tüm sütunlarla birlikte).
3. products tablosundan fiyatı en düşük 3 ürünü, sadece adları ve fiyatları ile getir.
4. customers tablosundaki en eski kayıtlı 10 müşteriyi signup_date'e göre sırala.
5. products tablosunda en fazla stoğa sahip ürünü sadece adı ve stock_quantity ile getir.
6. orders tablosunda son siparişi (tarihi en güncel olanı) listele.
7. products tablosunda sadece product_name sütununu alfabetik sırada göster.
8. customers tablosundan email sütunu olan ilk 5 müşteriyi customer_id'ye göre sırala.
9. orders tablosunda tutarı en düşük 3 siparişi ve bunların order_id'lerini getir.
10. customers tablosundan sadece Türkiye'deki (country = 'Turkey') müşterileri alfabetik sırala.
