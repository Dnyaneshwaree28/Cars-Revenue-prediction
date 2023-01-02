import pandas as pd 
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pickle
import numpy as np

st.set_page_config(page_title= "Dashboard" ,
                page_icon= "Plots:" ,
                layout= "wide")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.hdqwalls.com/wallpapers/black-ford-mustang-4k-2020-e7.jpg");
             background-attachment: fixed;
	     background-position:75%;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
cars = pd.read_csv("C:/Users/sansk/Downloads/carsEDA.csv")
model = pickle.load(open('C:/Users/sansk/Downloads/Regressor.pkl', 'rb'))



#-------SIDEBAR---------
# Dropdown list 

City_filter = st.sidebar.selectbox("Select the City", pd.unique(cars['City']))
Year_filter = st.sidebar.selectbox("Select the Year", pd.unique(cars['Year']))
# Types_filter = st.sidebar.selectbox("Select the Types", pd.unique(cars['Types']))
# Fuel_Type_filter = st.sidebar.selectbox("Select the Fuel_Type", pd.unique(cars['Fuel_Type']))
# Owner_filter = st.sidebar.selectbox("Select the Owner", pd.unique(cars['Owner']))
# Transmission_filter = st.sidebar.selectbox("Select the Transmission", pd.unique(cars['Transmission']))

cars = cars[cars['City']==City_filter]
cars = cars[cars['Year']==Year_filter]




#prediction code
if st.sidebar.button('Predict'):
    makeprediction = model.predict(pd.DataFrame(columns=['Name', 'Company', 'Transmission', 'Fuel_Type', 'City', 'Year', 'KM_Driven'],
                              data=np.array([Name, Company, Transmission, Fuel_Type, City, Year, KM_Driven]).reshape(1, 7)))
    output = round(makeprediction[0],2)
    st.success('Cars Price is {}'.format(output))

#--------MAINPAGE---------
st.title("Cars Price Prediction")
st.markdown("##")

#TOP KPI'S
Max_price = (cars["Sales_Price"].max())
average_Price = round(cars["Sales_Price"].mean(),1)
Average_Km = round(cars["KM_Driven"].mean(),1)

left_column , middle_column , right_column = st.columns(3)
with left_column:
    st.subheader("Maximum Price :")
    st.subheader(f"Rs {Max_price:,}")
with middle_column:
    st.subheader("Average Price :")
    st.subheader(f"Rs {average_Price:,}")
with right_column:
    st.subheader("Average_KM_DRIVEN:")
    st.subheader( f"km{Average_Km:,}")

st.markdown("____")

st.dataframe(cars)

#--------- Charts------------

fig_1 = px.bar(
    cars , x = "Sales_Price", y = "Fuel_Type",
    orientation="h",
    title="<b>Fuel_wise_sellingPrice</b>",

    color_discrete_sequence=["#0083B8"]*len(cars)
)





fig_2 = px.pie(cars , values = "Sales_Price" ,names = "Owner", title= "<b>Contribution of owner type</b>")

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_1 , use_container_width= True)
right_column.plotly_chart(fig_2 , use_container_width= True)

fig = px.scatter (cars , x= "Sales_Price" , y = "EMI(₹)" , color= "Company", symbol= "Fuel_Type"
, title="<b>Correlation between Variables</b>")

st.plotly_chart(fig)

fig_3 = px.box(cars ,x='Company',y='Sales_Price',  title= "<b>Company and Price</b>")
st.plotly_chart(fig_3)

fig_4 = px.violin(cars , x = "Company" , y = "KM_Driven" , title = "<b>Company and km_driven</b>" , orientation= "v")


fig_5= px.histogram(cars , x = "Year" , y = "Sales_Price",
                 title= "year vs price" )
                 

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_4 , use_container_width= True)
right_column.plotly_chart(fig_5 , use_container_width= True)





# ----------- HIDE STREAMLIT STYLE--------------
hide_st_style = """ 
               <style>
               #MainMenu {visibility : hidden;}
                footer {visibility : hidden;}
                </style>
                """
st.markdown(hide_st_style , unsafe_allow_html = True)               