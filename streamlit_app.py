import streamlit
import pandas
import snowflake.connector

streamlit.title("My Parents New Healthy Dinner")
print(" ") 
streamlit.header("BreakFast Menu")
streamlit.text("🥣 Omega 3 & Blue Berry Oat meal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard Boiled free Range Egg")
streamlit.text("🥑🍞 Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_select=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_select]
streamlit.dataframe(fruits_to_show)

streamlit.header("Snowflake User List")
conn = snowflake.connector.connect(
    user=streamlit.secrets["snowflake"]["user"],
    password=streamlit.secrets["snowflake"]["password"],
    account=streamlit.secrets["snowflake"]["account"],
    warehouse=streamlit.secrets["snowflake"].get("warehouse"),
    role=streamlit.secrets["snowflake"].get("role")
)
cur = conn.cursor()
try:
    cur.execute("SELECT name, login_name, created_on FROM SNOWFLAKE.ACCOUNT_USAGE.USERS ORDER BY name")
    user_df = cur.fetch_pandas_all()
    streamlit.dataframe(user_df)
finally:
    cur.close()
    conn.close()
