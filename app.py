import streamlit as st
from PIL import Image

def main():
    image = Image.open("data/food.jpg")
    st.image(image)
    st.markdown("# *Comfoodable*")

if __name__ == "__main__":
    main()
