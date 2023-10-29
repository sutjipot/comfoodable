import streamlit as st
from PIL import Image
from word2vec_dairyfree import get_df_recs
import unidecode
import nltk
from word2vec_glutenfree import get_gf_recs
from word2vec_mains import get_mains_recs
from word2vec_vegan import get_vegan_recs
from word2vec_vegetarian import get_vegetarian_recs


try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")


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
        st.session_state.choice = ""
    
    col1, col2 = st.beta_columns([1.8,4])
    with col1:
        select = st.selectbox("Choose dietary preference!", ["No restriction", "Vegan", "Vegetarian" ,"Dairy-free", "Gluten-free"])
        st.session_state.select = select
    with col2:
        ingredients = st.text_input(
            "Enter ingredients you have (seperate ingredients with a comma)",
            "chinese five spices, sirloin steak, feta cheese, bacon",)
        st.session_state.ingredients = ingredients
    st.text("")
    st.session_state.execute = st.button("Search recipes that match!")

    cola, colb, colc, cold, cole = [1,1,2,1,1]
    if st.session_state.execute:
        if select == "No restriction":
            recipe = get_mains_recs(ingredients, mean=True)
            st.session_state.clean = recipe.copy()
            recipe["url"] = recipe.apply(lambda row: clickable(row["recipe"], row["url"]), axis=1)
            recipe_display = recipe[["recipe", "time", "difficulty", "ingredients","url"]]
            st.session_state.recipe_display = recipe_display.to_html(escape=False)
            st.session_state.recipes = recipe.recipe.values.tolist()
            st.session_state.computed = True
            st.session_state.execute = False
            st.session_state.select = ""
            st.write(session_state.recipe_display, unsafe_allow_html=True)
            
        
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
