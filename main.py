import pandas as pd
import os

df = pd.read_excel("data/gelirgider.xlsx")

gelir = df[df['Tür']=='Gelir']['Tutar(₺)'].sum()
gider = df[df['Tür'] == 'Gider']['Tutar(₺)'].sum()
net= gelir-gider

print(df.head(5))
print(f"""Toplam geliriniz {gelir}₺.\nToplam gideriniz {gider}₺.\nNet karınız {net}₺.""")

def gunluk_ozet_raporu(df):
  df['Tarih'] = pd.to_datetime(df['Tarih']).dt.date
  gunluk = df.groupby(['Tarih', 'Tür'])['Tutar(₺)'].sum().unstack(fill_value=0)

  os.makedirs("outputs", exist_ok=True)
  
  with open("outputs/gunluk-ozet.txt", "w", encoding="utf-8") as f:
    for tarih, row in gunluk.iterrows():
      gelir = row.get('Gelir', 0)
      gider = row.get('Gider', 0)
      net_kar = gelir-gider

      gunun_giderleri = df[(df['Tarih'] == tarih) & (df['Tür'] == 'Gider')]
      if not gunun_giderleri.empty:
        en_fazla = gunun_giderleri.groupby('Kategori')['Tutar(₺)'].sum().idxmax()
      else:
        en_fazla = "Harcama Yok"
      
      f.write(f"""Tarih: {tarih}\nToplam Gelir: {gelir:.2f}₺\nToplam Gider: {gider:.2f}₺\nNet Kar: {net_kar:.2f}₺\nEn Fazla Harcama Yapılan: {en_fazla}\n\n---------------------------\n\n""")
      

gunluk_ozet_raporu(df)

from utils.grafikler import gunluk_gelir_gider_grafigi
gunluk_gelir_gider_grafigi(df)

from utils.grafikler import gider_kategorilerine_gore_pasta_grafigi
gider_kategorilerine_gore_pasta_grafigi(df)