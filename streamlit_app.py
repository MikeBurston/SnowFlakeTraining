import streamlit
streamlit.title('Your Choice of Food')

streamlit.header('☠️☠️☠️ Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.text('125% gratuity for parties of 4+')

streamlit.header('👽💩💩 Build Your Own Fruit Smoothie')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# display the table on top of the page
streamlit.dataframe(my_fruit_list)
