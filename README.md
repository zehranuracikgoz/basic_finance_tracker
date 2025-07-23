Proje Açıklaması
Finans işletmeleri için gelir-gider takip otomasyonu sağlayan bir Python projesidir. Günlük finansal hareketleri kaydeder, raporlar oluşturur ve görselleştirmeler sunar.

Özellikler
Günlük Gelir/Gider Takibi: Tarih bazında finansal hareket kaydı.
Otomatik Raporlama: Günlük özet raporları (txt formatında)
Veri Görselleştirme:
Gider kategorileri dağılımı
Günlük gelir-gider karşılaştırması
Excel Entegrasyonu: gelingider.xlsx üzerinden veri yönetimi


finanstrack
├── data/               # Veri dosyaları
│   └── gelirgider.xlsx # Ana excel veri kaynağı
├── utils/              # Yardımcı fonksiyonlar
│   └── grafikler.py    # Grafik oluşturma
├── main.py             # Ana uygulama
└── README.md 
├── outputs/            # Çıktılar
│   ├── grafikler/      # Verilerden oluşturulan grafikler
│   └── gunluk-ozet.txt # Metin raporu


Gereksinimler:
Excel İçin Zorunlu Sütunlar: Tarih, Tür (Gelir/Gider), Kategori, Tutar(₺)


Ana programı çalıştırdığınızda:
outputs/gunluk_ozet -> klasörüne günlük rapor oluşturulacak
outputs/grafikler/ -> altında görsel raporlar oluşturulacak


Örnek Çıktılar
Metin Raporu (gunluk-ozet.txt):

Tarih: 2023-01-01
Toplam Gelir: 1500.00₺
Toplam Gider: 750.00₺
Net Kar: 750.00₺
En Fazla Harcama Yapılan: Personel

Grafikler:
Gider kategorileri pasta grafiği (gider_kategorileri.png)
Günlük gelir-gider çubuk grafiği (gunluk_gelir_gider.png)