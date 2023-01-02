import streamlit as st



st.set_page_config(
    page_title="LR Project"
)

st.title("Price Prediction Online")
#st.image("")


st.sidebar.success("Select a page above.")

st.subheader("Choose a cars in cars24.com and \nfind best prediction to your \nfor any car model you choose \nsee all statestics over here \nThe site is build for help you to buy your dream car" )
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.hdqwalls.com/wallpapers/dark-side-car-digital-art-4k-2z.jpg");
             background-attachment: fixed;
	     background-position:75%;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
