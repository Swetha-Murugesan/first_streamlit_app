import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My Parents New Healthy diner')
streamlit.header('🍲Breakfast menu')

streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬kale, Spinach & Rocket Smoothy')
streamlit.text('🐔Hard-Boiled free range egg')
streamlit.text('🥑avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
# streamlit.dataframe(my_fruit_list)

fruits_selected=streamlit.multiselect("Pick Some fruites :",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#streamlit.dataframe(my_fruit_list)

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice) 
   fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
   
streamlit.header('Fruityvice Fruit Advice!')
try:
   fruit_choice=streamlit.text_input('what fruit would you like to infromation about?')
   if not fruit_choice:
       streamlit.error("Please select a fruit to get information.")
   else:
       back_from_function=get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
except URLError as e:
 streamlit.error()
streamlit.stop()
#import snowflake.connector

streamlit.header("Fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor()as my_cur:
       my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
       return my_cur.fetchall()
if streamlit.button('Get fruit Load_list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
# my_data_rows = my_cur.fetchall()
# streamlit.header("Fruit load list contains:")
# streamlit.dataframe(my_data_rows)

add_my_fruit=streamlit.text_input('what fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding',add_my_fruit)

my_cur.execute("insert into fruit_load_list values('from streamlit')")
