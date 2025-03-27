import streamlit as st
import json
import xmltodict
# import sys
# sys.path.append('./pages/Home.py')
# import pages
# import pages.Home as b

import pages.About
import pages.Home

# from pages import home

from streamlit_option_menu import option_menu

# import pages.mypackage.Home 
# st.title("Data science details.")
selected_menu = option_menu("",["Home","About","Project","Contact Us"],orientation="horizontal",icons=['house','envelope',"tools",'folder'],default_index=0)
st.html("<h1>HOME</h1>")
col1,col2,col3 = st.columns([1,0.3,1])
if selected_menu=="Home":
     # Home.pages
     pages.home()
     with open("Day 3.pdf",'rb'):
          st.download_button("donwload","Day 3.pdf")
          a = st.file_uploader("Add text file !")
          if a:
               for line in a:
                    
                    st.write(line)
                    print(line)
     
          # xml = a.read()
          # file1_data = json.loads(json.dumps(xmltodict.parse(xml)))
          # st.write(file1_data)
#           uploaded_files = st.file_uploader(
#     "Choose a CSV file", accept_multiple_files=True
# )
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)

# if selected_menu=='About':
#      pages.About()