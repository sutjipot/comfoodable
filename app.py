import streamlit as st
from PIL import Image

def main():
    st.markdown("# *:pizza::ramen: Comfoodable :bread::fork_and_knife:*")
    st.markdown("A content-based filtering ML for recipe recommendations by Indira Sutjipto and Ilona Nikkar")
    image = Image.open("data/food.jpg")
    st.image(image)
    st.markdown("## What should I make today? :yum:")
    st.markdown("I have a few ingredients at home.. I barely have time, but I have to cook! Let's use the tool below! :relieved:")
    

if __name__ == "__main__":
    main()
