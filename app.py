import streamlit as st
from PIL import Image

def main():
    st.markdown("# *Comfoodable :bread::fork_and_knife:*")
    image = Image.open("data/food.jpg")
    st.image(image)
    

if __name__ == "__main__":
    main()
