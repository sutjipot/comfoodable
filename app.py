import streamlit as st
from PIL import Image
from word2vec_dairyfree import get_df_recs
import unidecode
#from word2vec_glutenfree import get_gf_recs
#from word2vec_mains import get_mains_recs
#from word2vec_vegan import get_vegan_recs
#from word2vec_vegetarian import get_vegetarian_recs


def clickable(name, link):
    return f'<a target="_blank" href="{link}">{name}</a>'


def main():
    st.markdown("# *:pizza::ramen: Comfoodable :bread::fork_and_knife:*")
    st.markdown("Finding recipes made comfortable by Indira Sutjipto and Ilona Nikkar")
    image = Image.open("data/food.jpg")
    st.image(image)
    st.markdown("## What should I make today? :yum:")
    st.markdown("I have a few ingredients at home.. I barely have time, but I have to cook! Let's use the tool below! :relieved:")
    st.text("")

    if "execute" not in st.session_state:
        st.session_state.execute = False
        st.session_state.computed = False
        st.session_state.recipes = ""
        st.session_state.clean = ""
    
    
    col1, col2 = st.beta_columns([1.8,4])
    with col1:
        select = st.selectbox("Choose dietary preference!", ["No restriction", "Vegan", "Vegetarian" ,"Dairy-free", "Gluten-free"], placeholder="Select")
        st.session_state.select = select
    with col2:
        ingredients = st.text_input(
            "Enter ingredients you have (seperate ingredients with a comma)",
            "chinese five spices, sirloin steak, feta cheese, bacon",)
        st.session_state.ingredients = ingredients
    st.text("")
    st.session_state.execute = st.button("Search recipes that match!")

    if st.session_state.execute:
        if select == "No restriction":
            pass
        
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
