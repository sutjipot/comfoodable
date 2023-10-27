import streamlit as st
from PIL import Image
from streamlit_chat import message

def main():
    st.markdown("# *:pizza::ramen: Comfoodable :bread::fork_and_knife:*")
    st.markdown("A content-based filtering ML for recipe recommendations by Indira Sutjipto and Ilona Nikkar")
    image = Image.open("data/food.jpg")
    st.image(image)
    st.markdown("## What should I make today? :yum:")
    message("I have a few ingredients at home.. I barely have time, but I have to cook!", is_user = True)
    

if __name__ == "__main__":
    main()
