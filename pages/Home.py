import streamlit as st

def home():

    col1,col2,col3 = st.columns([1,0.3,1]) 
    with col1:
            st.header("Data Science")
            st.write("Data science is a multidisciplinary field that combines mathematics, statistics, computer science, and domain expertise to extract meaningful insights and knowledge from data, enabling informed decision-making and problem-solving")
        # with col2:st.header("")
    with col3:
            
            st.image('download.jpeg')

home()