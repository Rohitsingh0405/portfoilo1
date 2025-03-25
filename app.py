import streamlit as st
import sys
sys.path.append('./pages/Home.py')
import pages
import pages.Home as b



# from Home import home
from streamlit_option_menu import option_menu

# import pages.mypackage.Home 
# st.title("Data science details.")
selected_menu = option_menu("",["Home","About","Project","Contact Us"],orientation="horizontal",icons=['house','envelope',"tools",'folder'],default_index=0)
st.html("<h1>HOME</h1>")
col1,col2,col3 = st.columns([1,0.3,1])
if selected_menu=="Home":
     # Home.pages
     b.home()