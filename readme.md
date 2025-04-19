
# PostgreSQL Verileri Kullanılarak Doğrusal Regresyon Modeli Eğitimi ve Tahmin Uygulaması

## Proje Açıklaması

Bu proje, PostgreSQL veritabanında bulunan bir tablodaki verileri kullanarak doğrusal regresyon modeli oluşturur ve belirli bir değer için tahminde bulunur. Python dilinde hazırlanmış uygulama, PostgreSQL'deki verileri pandas ile çekerek, scikit-learn kütüphanesini kullanarak model eğitir.

## Kullanılan Teknolojiler ve Kütüphaneler

-   **Python**
    
-   **PostgreSQL**
    
-   **psycopg2** (PostgreSQL veritabanına bağlanmak için)
    
-   **pandas** (Veri işleme ve düzenleme için)
    
-   **scikit-learn** (Doğrusal regresyon modeli eğitimi için)
    
-   **numpy** (Sayısal işlemler için)
    

## Veritabanı Bağlantısı

PostgreSQL veritabanına bağlanmak için aşağıdaki bilgiler gereklidir:

-   `host`: PostgreSQL sunucusunun adresi
    
-   `port`: PostgreSQL bağlantı portu (varsayılan değer `5432`)
    
-   `database`: Veritabanının adı
    
-   `user`: Kullanıcı adı
    
-   `password`: Kullanıcının parolası
    

## Kullanılan Veritabanı Tablosu

Tablo adı: `test_data`

-   `x`: Bağımsız değişken, modelin girdisi.
    
-   `y`: Bağımlı değişken, modelin çıktısı.
    

## Uygulama Çalışma Adımları

1.  **PostgreSQL Bağlantısı:** Uygulama, PostgreSQL veritabanına bağlanarak verileri çeker.
    
2.  **Verilerin Alınması ve Kontrolü:**
    
    -   Tablodan `x` ve `y` verileri çekilir.
        
    -   Veriler pandas DataFrame formatında tutulur ve eksik değer kontrolü yapılır. Eksik değer varsa temizlenir.
        
3.  **Verilerin Model İçin Hazırlanması:**
    
    -   DataFrame'deki veriler bağımsız değişken (`X`) ve bağımlı değişken (`y`) olarak ayrılır.
        
4.  **Modelin Eğitilmesi:**
    
    -   Scikit-learn `LinearRegression` modeli kullanılarak eğitim gerçekleştirilir.
        
    -   Eğitim sonucunda katsayı (coefficient) ve sabit (intercept) bulunur.
        
5.  **Tahmin Yapma:**
    
    -   Eğitilen model ile yeni değer (`x=105`) için tahmin yapılır ve sonuç ekrana yazdırılır.
        

## Kullanım Talimatları

-   Python ve gerekli kütüphanelerin kurulu olduğundan emin olun:
    

```bash
pip install psycopg2 pandas scikit-learn numpy
```

-   Python scriptini çalıştırın:
    

```bash
python Postgres-LinearRegression.py
```

## Sonuçlar

-   Eğitilmiş doğrusal regresyon modelinin katsayıları ve tahmin edilen değer konsola yazdırılır.
    
-   Bu uygulama, PostgreSQL verilerini kullanarak basit bir regresyon modeli eğitmek ve tahmin yapmak isteyenlere örnek oluşturur.

## Yasin Bahadır ELibol
