import streamlit as st
from PIL import Image

def main():
    st.markdown("# *:pizza::ramen: Comfoodable :bread::fork_and_knife:*")
    image = Image.open("data/food.jpg")
    st.image(image, height=400)
    

if __name__ == "__main__":
    main()
