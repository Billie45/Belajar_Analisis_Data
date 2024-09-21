import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load data
days_df = pd.read_csv("./dashboard/clean_day.csv")
hours_df = pd.read_csv("./dashboard/clean_hour.csv")

# Mengonversi kolom 'date' menjadi datetime
days_df['date'] = pd.to_datetime(days_df['date'])
hours_df['date'] = pd.to_datetime(hours_df['date'])

# Mendapatkan rentang tanggal terendah dan tertinggi
min_date_days = days_df["date"].min()
max_date_days = days_df["date"].max()

##------------##
##    Title   ##
##------------##
st.title("Bike Sharing Analysis")

##----------------##
##    Side Bar    ##
##----------------##
with st.sidebar:
    st.header("Bike Sharing Analysis")
    st.image("https://media.istockphoto.com/id/1329906434/id/vektor/sistem-berbagi-sepeda-kota-terisolasi-di-atas-putih.jpg?s=612x612&w=0&k=20&c=4cx-qWCaUex8eQ7n7iq4_1jlgoBx0vVrUd2mPl8MZcE=")
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days])

# Filter dataset 
main_df_days = days_df[(days_df["date"] >= str(start_date)) & (days_df["date"] <= str(end_date))]
main_df_hour = hours_df[(hours_df["date"] >= str(start_date)) & (hours_df["date"] <= str(end_date))]

##--------------------##
##    Pertanyaan 1    ##
##--------------------##
st.subheader("Apakah jumlah penyewaan sepeda lebih banyak pada saat akhir pekan dibandingkan pada saat hari kerja?")

avg_rentals_by_weekend = main_df_days.groupby('is_weekend')['total_rentals'].mean().reset_index()
avg_rentals_by_weekend['is_weekend'] = avg_rentals_by_weekend['is_weekend'].map({0: 'Hari Kerja', 1: 'Akhir Pekan'})

# Membuat bar chart 
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='is_weekend', y='total_rentals', data=avg_rentals_by_weekend, dodge=False, color="Blue", ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda: Akhir Pekan vs Hari Kerja", fontsize=16)
ax.set_xlabel("Kategori Hari", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan Sepeda", fontsize=12)
st.pyplot(fig)

# Membuat Penjelasan 
st.write(f"Hari Kerja: {avg_rentals_by_weekend.loc[avg_rentals_by_weekend['is_weekend'] == 'Hari Kerja', 'total_rentals'].values[0]:.0f}")
st.write(f"Akhir Pekan: {avg_rentals_by_weekend.loc[avg_rentals_by_weekend['is_weekend'] == 'Akhir Pekan', 'total_rentals'].values[0]:.0f}")

st.write("**Conclusion**")
st.write("Rata-rata jumlah penyewaan sepeda pada hari kerja (4550 penyewa) sedikit lebih tinggi dibandingkan dengan akhir pekan (4389 penyewa). Meskipun banyak orang yang berasumsi bahwa penyewaan sepeda akan lebih tinggi di akhir pekan karena waktu luang, data menunjukkan bahwa orang lebih sering menyewa sepeda pada hari kerja.")

##--------------------##
##    Pertanyaan 2    ##
##--------------------##
st.subheader("Apakah hari libur menyebabkan peningkatan yang signifikan dalam jumlah penyewaan sepeda?")

avg_rentals_by_holiday = main_df_days.groupby('holiday')['total_rentals'].mean().reset_index()
avg_rentals_by_holiday['holiday'] = avg_rentals_by_holiday['holiday'].map({0: 'Hari Non-Libur', 1: 'Hari Libur'})

# Membuat bar chart 
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='holiday', y='total_rentals', data=avg_rentals_by_holiday, dodge=False, color="Blue", ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda: Hari Libur vs Non-Libur", fontsize=16)
ax.set_xlabel("Kategori Hari", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan Sepeda", fontsize=12) 
st.pyplot(fig)

# Membuat Penjelasan 
st.write(f"Hari Non-Libur: {avg_rentals_by_holiday.loc[avg_rentals_by_holiday['holiday'] == 'Hari Non-Libur', 'total_rentals'].values[0]:.0f}")
st.write(f"Hari Libur: {avg_rentals_by_holiday.loc[avg_rentals_by_holiday['holiday'] == 'Hari Libur', 'total_rentals'].values[0]:.0f}")

st.write("**Conclusion**")
st.write("Tidak ada peningkatan signifikan dalam jumlah penyewaan sepeda pada hari libur (3735 penyewa) dibandingkan hari biasa (4527 penyewa). berdasarkan hasil yang didapatkan, penyewaan sepeda cenderung turun pada hari libur dibandingkan hari biasa.")

##--------------------##
###   Pertanyaan 3    ##
##--------------------##
st.subheader("Apakah pengguna registered menyewa sepeda secara stabil setiap hari sementara pengguna casual lebih bervariasi?")

avg_rentals_by_user_type = main_df_hour.groupby('is_weekend')[['casual', 'registered']].mean().reset_index()
avg_rentals_by_user_type['is_weekend'] = avg_rentals_by_user_type['is_weekend'].map({0: 'Hari Kerja', 1: 'Akhir Pekan'})

avg_rentals_melted = avg_rentals_by_user_type.melt(id_vars='is_weekend', value_vars=['casual', 'registered'], var_name='User Type', value_name='Rata-rata Penyewaan')

# Membuat bar chart 
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='is_weekend', y='Rata-rata Penyewaan', hue='User Type', data=avg_rentals_melted, palette="Set1", ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda: Casual vs Registered", fontsize=16)
ax.set_xlabel("Kategori Hari", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan", fontsize=12)
st.pyplot(fig)

# Membuat Penjelasan 
st.write(f"Casual (Hari Kerja): {avg_rentals_by_user_type.loc[avg_rentals_by_user_type['is_weekend'] == 'Hari Kerja', 'casual'].values[0]:.0f}")
st.write(f"Casual (Akhir Pekan): {avg_rentals_by_user_type.loc[avg_rentals_by_user_type['is_weekend'] == 'Akhir Pekan', 'casual'].values[0]:.0f}")
st.write(f"Registered (Hari Kerja): {avg_rentals_by_user_type.loc[avg_rentals_by_user_type['is_weekend'] == 'Hari Kerja', 'registered'].values[0]:.0f}")
st.write(f"Registered (Akhir Pekan): {avg_rentals_by_user_type.loc[avg_rentals_by_user_type['is_weekend'] == 'Akhir Pekan', 'registered'].values[0]:.0f}")

st.write("**Conclusion**")
st.write("Pengguna registered cenderung lebih stabil dalam hal penyewaan sepeda, dengan jumlah penyewaan yang lebih konsisten antara hari kerja dan akhir pekan. walaupun terdapat penurunan pada akhir pekan, jumlahnya tidak terlalu signifikan.")
st.write("Pengguna casual menunjukkan variasi yang lebih besar, dengan peningkatan yang signifikan dalam penyewaan selama akhir pekan.")

##----------------##
##    Copyright   ##
##----------------##
st.markdown("© 2024 Billie Zandra Widiyanto. All rights reserved.")