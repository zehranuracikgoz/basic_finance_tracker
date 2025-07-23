import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def gunluk_gelir_gider_grafigi(df):
  df['Tarih'] = pd.to_datetime(df["Tarih"]).dt.date
  gunluk_ozet = df.groupby(['Tarih', 'Tür']) ['Tutar(₺)'].sum().unstack()

  os.makedirs("outputs/grafikler", exist_ok=True)
 
  plt.figure(figsize=(10,6))
  ax = gunluk_ozet.plot(kind='bar', stacked= False, ax=plt.gca())

  plt.title("Günlük Gelir ve Gider")
  plt.ylabel("Tutar (₺)")
  plt.xlabel("Tarih")
  plt.xticks(rotation=45)
  plt.tight_layout()

  for p in ax.patches:
    height = p.get_height()
    if pd.notnull(height) and height != 0:
        ax.text(p.get_x() + p.get_width()/2,
                height + 1, f'{height:.0f}',
                ha='center',  va = 'bottom' if height > 0 else 'top',
                fontweight='bold', color='black', fontsize=8)


  plt.savefig("outputs/grafikler/gunluk_gelir_gider.png")
  plt.close()



def gider_kategorilerine_gore_pasta_grafigi(df):
  df['Tarih'] = pd.to_datetime(df["Tarih"])
  gider_df= df[df['Tür']== 'Gider']

  kategori_toplam = gider_df.groupby('Kategori') ['Tutar(₺)'].sum()

  os.makedirs("outputs/grafikler", exist_ok=True)
  plt.figure(figsize=(8,8))
  plt.pie(kategori_toplam, labels=kategori_toplam.index, autopct='%1.2f%%', startangle=90)
  plt.title('Kategorilere Göre Gider Dağılımı')
  plt.axis('equal')
  plt.tight_layout()
  plt.savefig("outputs/grafikler/gider_kategorileri.png")
  plt.close()
