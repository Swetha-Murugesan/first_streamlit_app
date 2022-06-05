import streamlit
streamlit.title('My Parents New Healthy diner')
streamlit.header('🍲Breakfast menu')

streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬kale, Spinach & Rocket Smoothy')
streamlit.text('🐔Hard-Boiled free range egg')
streamlit.text('🥑avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick Some fruites :",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
