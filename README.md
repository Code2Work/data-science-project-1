# Data Science SQL Project 1 - THE BASICS

## Proje Kurulumu

1. Projeyi **fork** edin ve kendi hesabınıza **clone** edin.
2. Terminal'de proje klasörüne girin.

### Mac / Linux
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Veritabanı Kurulumu

Soruları çözebilmek için önce local PostgreSQL veritabanınızda tabloları oluşturmanız gerekiyor:

1. PostgreSQL'in bilgisayarınızda kurulu ve çalışır durumda olduğundan emin olun.
2. `scripts/init_db.py` dosyasındaki SQL komutlarını sırasıyla kendi local veritabanınızda çalıştırın.
3. Tabloların doğru oluştuğundan emin olmak için her tabloya birer `SELECT *` sorgusu atın.

> **Not:** `data/questions.py` içindeki `connect_db()` fonksiyonunda veritabanı bağlantı bilgileri var.
> Localinizde test ederken kendi bilgilerinizle değiştirin.
> **Pushlarken bu bilgileri varsayılan haliyle bırakın** (CI/CD ortamında bu bilgilerle çalışıyor).

## Başlangıç Ayarları

Kodlamaya başlamadan önce şu iki dosyada kendi bilgilerinizi güncellemeniz gerekiyor:

1. **`tests/test_question.py`** — Dosyanın altındaki `run_tests()` fonksiyonunda `user_id` değerini **kendi kullanıcı ID'nizle** değiştirin.
2. **`data/questions.py`** — `connect_db()` fonksiyonundaki veritabanı şifresini kendi local PostgreSQL şifrenizle değiştirin. **Pushlarken varsayılan haliyle bırakın.**

## Çalışma Şekli

- Sadece `data/questions.py` dosyasında çalışın.
- Her `question_X_query()` fonksiyonu içindeki boş `cursor.execute('')` satırına SQL sorgunuzu yazın.
- Diğer dosyaları değiştirmeyin.

## Testleri Çalıştırma

```bash
python watch.py
```

Bu komut dosya değişikliklerini izler ve her kaydettiğinizde testleri otomatik çalıştırır.

Tek seferlik çalıştırmak için:
```bash
pytest tests/test_question.py -s -v
```

## Tablolar

### customers
| Sütun | Tip |
|-------|-----|
| customer_id | SERIAL (PK) |
| customer_name | VARCHAR(100) |
| email | VARCHAR(100) |
| country | VARCHAR(50) |
| signup_date | DATE |

### products
| Sütun | Tip |
|-------|-----|
| product_id | SERIAL (PK) |
| product_name | VARCHAR(100) |
| price | NUMERIC(8,2) |
| stock_quantity | INTEGER |

### orders
| Sütun | Tip |
|-------|-----|
| order_id | SERIAL (PK) |
| customer_id | INTEGER (FK -> customers) |
| order_date | DATE |
| total_amount | NUMERIC(10,2) |

## Sorular

1. **customers** tablosundan tüm müşterilerin **adlarını ve ülkelerini** getir.

2. **orders** tablosundaki en yüksek tutarlı **5 siparişi**, tüm sütunlarıyla birlikte listele. (`total_amount`'a göre azalan sırada)

3. **products** tablosundan fiyatı en düşük **3 ürünü**, sadece **adları ve fiyatları** ile getir.

4. **customers** tablosundaki tüm müşterileri `signup_date`'e göre **eskiden yeniye** sırala. (Tüm sütunlar, LIMIT 10)

5. **products** tablosunda en fazla stoğa sahip ürünü, sadece **adı ve stock_quantity** ile getir. (1 kayıt)

6. **orders** tablosundaki **son siparişi** (tarihi en güncel olan) tüm sütunlarıyla listele. (1 kayıt)

7. **products** tablosundan sadece `product_name` sütununu **alfabetik sırada** getir.

8. **customers** tablosundan `customer_id`'ye göre sıralanmış ilk **5 müşteriyi**, sadece `customer_id` ve `email` sütunlarıyla getir.

9. **orders** tablosundaki tutarı en düşük **3 siparişi**, sadece `order_id` ve `total_amount` ile getir. (`total_amount`'a göre artan sırada)

10. **customers** tablosundan sadece **Türkiye'deki** (`country = 'Turkey'`) müşterileri `customer_name`'e göre **alfabetik** sırala. (Tüm sütunlar)

---

## İpucu: Ayrı Schema Kullanmak

Localinizdeki PostgreSQL'de başka tablolarla karışmasın istiyorsanız, yeni bir schema oluşturabilirsiniz:

```sql
CREATE SCHEMA data1;
```

Ardından `scripts/init_db.py` içindeki tablo isimlerinin başına schema adını ekleyin:

```sql
CREATE TABLE data1.customers ( ... );
CREATE TABLE data1.products ( ... );
CREATE TABLE data1.orders ( ... );
```

Foreign key (REFERENCES) tanımlarında da schema adını eklemeyi unutmayın:

```sql
CREATE TABLE data1.orders (
    ...
    customer_id INTEGER REFERENCES data1.customers(customer_id),
    ...
);
```

Sorgularınızda da aynı şekilde schema adını kullanmayı unutmayın:

```sql
SELECT * FROM data1.customers;
```

> **Önemli:** Bu sadece localinizde çalışırken kolaylık için. Kodunuzu pushlarken schema öneki olmadan bırakın, CI/CD ortamında `public` schema kullanılıyor.
