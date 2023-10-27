import streamlit as st
from PIL import Image

def main():
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
            <h1 style="text-align: center;">*Comfoodable*</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    image = Image.open("data/food.jpg")
    st.image(image)
    

if __name__ == "__main__":
    main()
