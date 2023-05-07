import streamlit
import pandas

streamlit.title("My Parents New Healthy Dinner")
print(" ") 
streamlit.header("BreakFast Menu")
streamlit.text("🥣 Omega 3 & Blue Berry Oat meal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard Boiled free Range Egg")
streamlit.text("🥑🍞 Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
