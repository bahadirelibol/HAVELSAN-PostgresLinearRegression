import psycopg2
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def main():
    """
    PostgreSQL'den veri çekerek doğrusal regresyon modeli oluşturur ve tahmin yapar.
    """
    # PostgreSQL bağlantısı için gerekli parametreler
    try:
        conn = psycopg2.connect(
            host=" ",                # PostgreSQL sunucu adresi
            port=5432,               # PostgreSQL portu (varsayılan: 5432)
            database="postgres",     # Veritabanı adı
            user="postgres",         # Kullanıcı adı
            password=" "             # Parola
        )
    except psycopg2.Error as e:
        print(f"Veritabanına bağlanırken hata oluştu: {e}")
        return

    # test_data tablosundan verilerin çekilmesi
    try:
        query = "SELECT x, y FROM test_data ORDER BY x"
        df = pd.read_sql(query, conn)
    except pd.DatabaseError as e:
        print(f"Veri çekme sırasında hata oluştu: {e}")
        conn.close()
        return
    conn.close()

    # Veri Doğrulama ve Temizlik
    if df.isnull().any().any():
        print("Verilerde eksik (NULL) değerler bulundu. Verileri temizliyorum...")
        df = df.dropna()  # Eksik verileri sil
    if len(df) == 0:
        print("Veri seti boş. Lütfen verileri kontrol edin.")
        return

    # Verileri model için hazırlama
    try:
        X = df[['x']]  # Bağımsız değişken (girdi)
        y = df['y']    # Bağımlı değişken (çıktı)
    except KeyError as e:
        print(f"Veri sütunlarında hata: {e}. 'x' ve 'y' sütunlarının var olduğundan emin olun.")
        return

    # Basit linear regresyon modelinin eğitilmesi
    try:
        model = LinearRegression()
        model.fit(X, y)
    except Exception as e:
        print(f"Model eğitimi sırasında hata oluştu: {e}")
        return

    # Eğitilmiş katsayı ve sabitin yazdırılması
    print("Eğitimli katsayı (Coefficient):", model.coef_[0])
    print("Eğitilmiş sabit (Intercept):", model.intercept_)

    # Test tahmin: x = 105 olan y değerinin tahmini
    try:
        x_test = np.array([[105]])
        y_pred = model.predict(x_test)
        print("x=105 için tahmin edilen y değeri:", y_pred[0])
    except Exception as e:
        print(f"Tahmin sırasında hata oluştu: {e}")
        return

if __name__ == "__main__":
    main()