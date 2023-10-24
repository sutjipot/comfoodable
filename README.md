# Comfoodable: Recipe Reccommendation System
Finding recipes made comfortable

## Overview
A recipe reccommendation system tailored to every user's wants and needs.
Comfoodable returns reccommended recipes based on user's limitations (vegan, vegetarian, gluten-free, dairy-free, or none) and available ingredients, and users can choose best-fitted recipes to try. Comfoodable also shows user the difficulty and time needed to make the recipes to aid users with better decision making.
- Python and BeautifulSoup were used to scrape over 3000 recipes from [Jamie Oliver](https://www.jamieoliver.com/).
- Word2Vec and TF-IDF were used to create word embeddings of the parsed ingredients.
- Cosine-similarity was used to measure the similarity of two vectors (recipe ingredients and user input ingredients).
- Streamlit was used to create an interactable app for users.

## Motivation
To start, a human's main needs are food, clothing, and shelter. What separates food from the other two is the fact that one needs to make or buy food every single day, which is not the case for shelter and clothing. For something that must be prepared every single day (in this case, cooking), one would need availability in time and ingredients. Sometimes one has the time but not the ingredients, or vice-versa. This pushes me to making a recipe reccommendation system. But, I myself have dietary limitations, and cannot seem to find the best recipe for myself. That is what motivated me to add a dietary preference feature.


