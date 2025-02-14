import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

st.set_page_config(page_title="E-Commerce Public Dataset Analysis",
page_icon=":snow_capped_mountain", layout='wide')

all_df = pd.read_csv('all_data.csv')

product_counts = all_df.groupby('product_category_name_english')['product_id'].count().reset_index()
sorted_df = product_counts.sort_values(by='product_id', ascending=False)

city_seller = all_df.seller_city.value_counts().sort_values(ascending=False).rename_axis('City').reset_index(name='Number of Sellers')

city_customer = all_df.customer_city.value_counts().sort_values(ascending=False).rename_axis('City').reset_index(name='Number of Customers')

total_payment_type = all_df.groupby('payment_type')['payment_value'].sum().reset_index()





with st.container():
  left_col, right_col = st.columns(2)
  
  with left_col:
    st.subheader('E-Commerce Pubilc Dataset Analysis')
    st.markdown(
      "Kelompok 5")

    with st.expander("Anggota"):
      st.write("10123085 - Muhamad Rizki Fadilah")
      st.write("10123086 - Daffa Firizqi")
      st.write("10123098 - Arya Manggala")
      st.write("10123106 - Randy Fawwaz Aditya")
      st.write("10123125 - Nabila Syifa Az Zahra")
      st.write("10123126 - Taufik Alimansyah")

with st.container():
  st.write("---")
  st.subheader("Apa produk yang paling banyak dibeli dan paling sedikit dibeli?")

  fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

  colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

  sns.barplot(x="product_id", y="product_category_name_english", hue="product_category_name_english", data=sorted_df.head(5), palette=colors, ax=ax[0])
  ax[0].set_ylabel(None)
  ax[0].set_xlabel(None)
  ax[0].set_title("Produk yang paling banyak dibeli", loc="center", fontsize=19)
  ax[0].tick_params(axis='y', labelsize=15)

  sns.barplot(x="product_id", y="product_category_name_english", hue="product_category_name_english", data=sorted_df.sort_values(by="product_id", ascending=True).head(5), palette=colors, ax=ax[1])
  ax[1].set_ylabel(None)
  ax[1].set_xlabel(None)
  ax[1].invert_xaxis()
  ax[1].yaxis.set_label_position("right")
  ax[1].yaxis.tick_right()
  ax[1].set_title("Produk yang paling sedikit dibeli", loc="center", fontsize=19)
  ax[1].tick_params(axis='y', labelsize=15)

  plt.suptitle("Produk yang paling banyak dan sedikit dibeli", fontsize=28)
  
  st.pyplot(fig)

  with st.expander("Lihat Penjelasan"):
    st.write("""Berdasarkan data yang tertera produk yang paling banyak dibeli adalah bed_bath_table dan produk yang paling sedikit dibeli adalah security_and_service.""")

with st.container():
  st.write("---")
  st.subheader("Bagaimana tingkat kepuasan pembeli terhadap layanan?")
  
  rating_service = all_df['review_score'].value_counts().sort_values(ascending=False)
  ax_score = rating_service.idxmax()
  
  sns.set(style="darkgrid")

  plt.figure(figsize=(10, 5))
  sns.barplot(x=rating_service.index,
              y=rating_service.values,
              order=rating_service.index
              )

  plt.title("Penilaian Customer terhadap Pelayanan", fontsize=15)
  plt.xlabel("Rating")
  plt.ylabel("Customer")
  plt.xticks(fontsize=12)

  st.pyplot(plt)

  with st.expander("Lihat Penjelasan"):
    st.write("""Berdasarkan data yang tertera lebih dari 60.000 pembeli yang merasa puas terhadap pelayanan yang diberikan.""")

with st.container():
  st.write("---")
  st.subheader("Kota mana yang memiliki seller paling banyak?")
  
  top_5_cities = city_seller.head(5)
  plt.figure(figsize=(10, 6))
  colors = ["#72BCD4" if city == top_5_cities['City'].iloc[0] else "#D3D3D3" for city in top_5_cities['City']]
  sns.barplot(x="Number of Sellers", y="City", data=top_5_cities, hue=top_5_cities['City'], palette=colors, legend=False)
  plt.xlabel('Jumlah Penjual')
  plt.ylabel('Kota')
  plt.title('5 Kota dengan Penjual Terbanyak')

  st.pyplot(plt)

  with st.expander("Lihat Penjelasan"):
    st.write("""Kota San Paulo dengan seller yang berjumlah 29.293 orang.""")

with st.container():
  st.write("---")
  st.subheader("Kota mana yang memiliki customer paling banyak?")

  top_5_cities_customer = city_customer.head(5)
  plt.figure(figsize=(10, 6))
  colors = ["#72BCD4" if city == top_5_cities_customer['City'].iloc[0] else "#D3D3D3" for city in top_5_cities_customer['City']]
  sns.barplot(x="Number of Customers", y="City", data=top_5_cities_customer, hue=top_5_cities_customer['City'], palette=colors, legend=False)
  plt.xlabel('Jumlah Customer')
  plt.ylabel('Kota')
  plt.title('5 Kota dengan Customer Terbanyak')

  st.pyplot(plt)

  with st.expander("Lihat Penjelasan"):
    st.write("""Kota San Paulo dengan customer yang berjumlah 18.875 orang.""")




