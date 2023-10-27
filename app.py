import streamlit as st
from PIL import Image

def main():
    st.markdown(
        """
        <div style="justify-content: center; align-items: center;>
            <h1 style="text-align: center;">Comfoodable</h1>
        </div>
        """
    )
    image = Image.open("data/food.jpg")
    st.image(image)
    

if __name__ == "__main__":
    main()
