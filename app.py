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
        select = st.selectbox("Choose dietary preference!", ["No restriction", "Vegan", "Vegetarian" ,"Dairy-free", "Gluten-free"], placeholder="Select")
        st.session_state.select = select
    with col2:
        ingredients = st.text_input(
            "Enter ingredients you have (seperate ingredients with a comma)",
            "chinese five spices, sirloin steak, feta cheese, bacon",)
        st.session_state.ingredients = ingredients
    st.text("")
    search = st.button("Search recipes that match!")

    if search:
        if select and ingredients:
            if select == "No restriction":
                st.write("yeyeye")
            elif select == "Vegan":
                pass
            elif select == "Vegetarian":
                pass
            elif select == "Gluten-free":
                pass
            else:
                pass



if __name__ == "__main__":
    main()
