# Data Science SQL Project 1 - THE BASICS

## Proje Kurulumu

1. Projeyi **fork** edin ve kendi hesabiniza **clone** edin.
2. Terminal'de proje klasorune girin.

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

## Veritabani Kurulumu

Sorulari cozebilmek icin once local PostgreSQL veritabaninizda tablolari olusturmaniz gerekiyor:

1. PostgreSQL'in bilgisayarinizda kurulu ve calisir durumda oldugundan emin olun.
2. `scripts/init_db.py` dosyasindaki SQL komutlarini sirasiyla kendi local veritabaninizda calistirin.
3. Tablolarin dogru olustugundan emin olmak icin her tabloya birer `SELECT *` sorgusu atin.

> **Not:** `data/questions.py` icindeki `connect_db()` fonksiyonunda veritabani baglanti bilgileri var.
> Localinizde test ederken kendi bilgilerinizle degistirin.
> **Pushlarken bu bilgileri varsayilan haliyle birakin** (CI/CD ortaminda bu bilgilerle calisiyor).

## Baslangic Ayarlari

Kodlamaya baslamadan once su iki dosyada kendi bilgilerinizi guncellemeniz gerekiyor:

1. **`tests/test_question.py`** — Dosyanin altindaki `run_tests()` fonksiyonunda `user_id` degerlerini **kendi bilgilerinizle** degistirin.
2. **`data/questions.py`** — `connect_db()` fonksiyonundaki veritabani sifresini kendi local PostgreSQL sifrenizle degistirin. **Pushlarken varsayilan haliyle birakin.**

## Calisma Sekli

- Sadece `data/questions.py` dosyasinda calisin.
- Her `question_X_query()` fonksiyonu icindeki bos `cursor.execute('')` satirina SQL sorgunuzu yazin.
- Diger dosyalari degistirmeyin.

## Testleri Calistirma

```bash
python watch.py
```

Bu komut dosya degisikliklerini izler ve her kaydettiginizde testleri otomatik calistirir.

Tek seferlik calistirmak icin:
```bash
pytest tests/test_question.py -s -v
```

## Tablolar

### customers
| Sutun | Tip |
|-------|-----|
| customer_id | SERIAL (PK) |
| customer_name | VARCHAR(100) |
| email | VARCHAR(100) |
| country | VARCHAR(50) |
| signup_date | DATE |

### products
| Sutun | Tip |
|-------|-----|
| product_id | SERIAL (PK) |
| product_name | VARCHAR(100) |
| price | NUMERIC(8,2) |
| stock_quantity | INTEGER |

### orders
| Sutun | Tip |
|-------|-----|
| order_id | SERIAL (PK) |
| customer_id | INTEGER (FK -> customers) |
| order_date | DATE |
| total_amount | NUMERIC(10,2) |

## Sorular

1. **customers** tablosundan tum musterilerin **adlarini ve ulkelerini** getir.

2. **orders** tablosundaki en yuksek tutarli **5 siparisi**, tum sutunlariyla birlikte listele. (`total_amount`'a gore azalan sirada)

3. **products** tablosundan fiyati en dusuk **3 urunu**, sadece **adlari ve fiyatlari** ile getir.

4. **customers** tablosundaki tum musterileri `signup_date`'e gore **eskiden yeniye** sirala. (Tum sutunlar, LIMIT 10)

5. **products** tablosunda en fazla stoga sahip urunu, sadece **adi ve stock_quantity** ile getir. (1 kayit)

6. **orders** tablosundaki **son siparisi** (tarihi en guncel olan) tum sutunlariyla listele. (1 kayit)

7. **products** tablosundan sadece `product_name` sutununu **alfabetik sirada** getir.

8. **customers** tablosundan `customer_id`'ye gore siralanmis ilk **5 musteriyi**, sadece `customer_id` ve `email` sutunlariyla getir.

9. **orders** tablosundaki tutari en dusuk **3 siparisi**, sadece `order_id` ve `total_amount` ile getir. (`total_amount`'a gore artan sirada)

10. **customers** tablosundan sadece **Turkiye'deki** (`country = 'Turkey'`) musterileri `customer_name`'e gore **alfabetik** sirala. (Tum sutunlar)

---

## Ipucu: Ayri Schema Kullanmak

Localinizdeki PostgreSQL'de baska tablolarla karismasin istiyorsaniz, yeni bir schema olusturabilirsiniz:

```sql
CREATE SCHEMA data1;
```

Ardindan `scripts/init_db.py` icindeki tablo isimlerinin basina schema adini ekleyin:

```sql
CREATE TABLE data1.customers ( ... );
CREATE TABLE data1.products ( ... );
CREATE TABLE data1.orders ( ... );
```

Foreign key (REFERENCES) tanimlarinda da schema adini eklemeyi unutmayin:

```sql
CREATE TABLE data1.orders (
    ...
    customer_id INTEGER REFERENCES data1.customers(customer_id),
    ...
);
```

Sorgularinizda da ayni sekilde schema adini kullanmayi unutmayin:

```sql
SELECT * FROM data1.customers;
```

> **Onemli:** Bu sadece localinizde calisirken kolaylik icin. Kodunuzu pushlarken schema oneki olmadan birakin, CI/CD ortaminda `public` schema kullaniliyor.
