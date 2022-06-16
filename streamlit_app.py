import streamlit
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#defines fruit list index as the names of the fruit as opposed to their ID number
my_fruit_list = my_fruit_list.set_index('Fruit')

#allows user to pick fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))


#displays table on the page
streamlit.dataframe(my_fruit_list)

