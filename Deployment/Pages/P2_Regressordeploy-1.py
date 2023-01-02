import pickle
import streamlit as st
import pandas as pd
import numpy as np

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
cars = pd.read_csv('C:/Users/sansk/Downloads/carsEDA.csv')
model = pickle.load(open('C:/Users/sansk/Downloads/Regressor.pkl', 'rb'))


def main():
    st.title('Cars Price Prediction')

    #input variables
    Name = st.selectbox("Name", cars['Name'].unique())
    Company = st.selectbox("Company", cars['Company'].unique())
    Transmission = st.selectbox("Transmission", cars['Transmission'].unique())
    Fuel_Type = st.selectbox("Fuel_Type", cars['Fuel_Type'].unique())
    City = st.selectbox("City", cars['City'].unique())
    Year = st.selectbox("Year", cars['Year'].unique())
    KM_Driven= st.selectbox("KM_Driven", cars['KM_Driven'].unique())

    #prediction code
    if st.button('Predict'):
        makeprediction = model.predict(pd.DataFrame(columns=['Name', 'Company', 'Transmission', 'Fuel_Type', 'City', 'Year', 'KM_Driven'],
                              data=np.array([Name, Company, Transmission, Fuel_Type, City, Year, KM_Driven]).reshape(1, 7)))
        output = round(makeprediction[0],2)
        st.success('Cars Price is {}'.format(output))

if __name__=='__main__':
    main()
