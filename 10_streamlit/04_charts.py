import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# 한글 폰트 설정
plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False

st.title("04. 차트")

months = pd.date_range("2024-01-01", periods=12, freq="ME")
sales = np.random.randint(20000, 50000, size=12)

df = pd.DataFrame({
    "월": months.strftime("%Y-%m"),
    "매출": sales
})

st.subheader("1) st.line_chart")
st.line_chart(df.set_index("월"))

st.subheader("2) st.bar_chart")
st.bar_chart(df.set_index("월"))

st.subheader("3) Matplotlib : 원하는대로 커스터마이징")
fig, ax = plt.subplots()
ax.plot(df["월"], df["매출"], marker="o")
ax.set_title("월별 매출(예시)")
ax.set_xlabel("월")
ax.set_ylabel("매출")
plt.xticks(rotation=45)  # x축 레이블이 겹치지 않도록 45도 회전

st.pyplot(fig, width="stretch")