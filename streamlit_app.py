import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('my parants new healthy dinner')

streamlit.header('Breakfast Favorate')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#create function
def get_fruitvise_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# Display the table on the page.
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please setect a fruit to get information.")
  else:
    back_from_function = get_fruitvise_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()



streamlit.header("The Fruit load list contains:")
#snowflake function
def get_fruit_load_list():
    with my_cnx.cursor() as my_curr:
        my_cur.execute("SELECT * FROM fruit_load_list")
        return my_cur.fetchall()
    
#add a button to load data
if streamlit.button('Get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)


      
streamlit.stop()
add_new_fruit = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('The user entered ', add_new_fruit)

Streamlit.write('Thanks for additing', add_new_fruit)

my_curr.execute("Insert into fruit_load_list values ('my streamlit')")
