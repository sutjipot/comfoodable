import streamlit as st

def main():
    image = Image.open("data/food.jpg").resize((680, 150))
    st.image(image)
    st.markdown("# *Comfoodable*")

if __name__ == "__main__":
    main()
