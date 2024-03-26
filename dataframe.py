# -*- coding:utf-8 -*-
import streamlit as st # 배포
import pandas as pd # 그래프
import matplotlib.pyplot as plt
import seaborn as sns # 시각화 하기 위해 라이브러리에서 두개 가져옴(위, 옆)

@st.cache_data
def load_data():
    df = pd.read_csv("gapminder.tsv", sep="\t") # dataFrame, 데이터를 불러들인다
    return df

def plot_matplotlib(): # streamlit 문법에 맞게 작성
    st.title("Categorical Bar Plot with Seaborn") # 대시보드 제목
    df = load_data()
    fig, ax = plt.subplots() # 시각화하는 메소드
    
    # Using Seaborn's barplot function
    sns.barplot(x=df['year'], y=df['lifeExp'], data=df, ax=ax)
    
    # Labeling axes and title
    ax.set_xlabel("year")
    ax.set_ylabel("lifeExp")
    ax.set_title("Year vs lifeExp")
    
    st.pyplot(fig) # 대시보드에 출력

def main():
    st.title("Data Display st.dataframe()")
    st.checkbox("Use container width", value=False, key = 'use_container_width')
    
    df = load_data()
    st.dataframe(df, use_container_width=True) # 대시보드에 표 삽입

    #pandas style 두번째 표
    st.tite("Maximum value per column")
    st.dataframe(df.iloc[:5,2:].style.highlight_max(axis=0)) # 행에서 가장 큰 값을 하이라이트해서 보여줘라

    plot_matplotlib() # 그래프 삽입
    
    
if __name__ == "__main__":
    main()