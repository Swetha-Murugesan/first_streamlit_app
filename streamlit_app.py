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
# streamlit.dataframe(my_fruit_list)

fruits_selected=streamlit.multiselect("Pick Some fruites :",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#streamlit.dataframe(my_fruit_list)

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice-streamlit.text_input('what fruit would you like to infromation about?','kiwi')
streamlit.write('The user entered',fruit_choice)

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+"kiwi") 
#streamlit.text(fruityvice_response.json())

fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
