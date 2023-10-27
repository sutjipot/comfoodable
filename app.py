import streamlit as st
from PIL import Image

def main():
    st.markdown("# *:pizza::ramen: Comfoodable :bread::fork_and_knife:*")
    st.markdown("A content-based filtering ML for recipe recommendations by Indira Sutjipto and Ilona Nikkar")
    image = Image.open("data/food.jpg")
    st.image(image)
    st.markdown("## What should I make today? :yum:")
    st.markdown("I have a few ingredients at home.. I barely have time, but I have to cook! Let's use the tool below! :relieved:")
    st.text("")

    col1, col2 = st.columns([1.8,4])
    with col1:
        select = st.selectbox("Choose your dietary preference!", ["No restriction", "Vegan", "Vegetarian" ,"Dairy-free", "Gluten-free"])
    with col2:
        ingredients = st.text_input(
            "Enter ingredients you would like to cook with (seperate ingredients with a comma)",
            "chinese five spices, sirloin steak, feta cheese, bacon",)
    st.text("")
    st.button("Search")

if __name__ == "__main__":
    main()
