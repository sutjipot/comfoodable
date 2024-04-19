# [Comfoodable](https://comfoodable.streamlit.app/): Recipe Recommendation System 
Finding recipes made comfortable

## Overview
A recipe recommendation system tailored to every user's wants and needs.
Comfoodable returns recommended recipes based on user's limitations (vegan, vegetarian, gluten-free, dairy-free, or none) and available ingredients, and users can choose best-fitted recipes to try. Comfoodable also shows user the difficulty and time needed to make the recipes to aid users with better decision making.
- Python and BeautifulSoup were used to scrape over 3000 recipes from [Jamie Oliver](https://www.jamieoliver.com/).
- Word2Vec and TF-IDF were used to create word embeddings of the parsed ingredients.
- Cosine-similarity was used to measure the similarity of two vectors (recipe ingredients and user input ingredients).
- Streamlit was used to create an interactable app for users.

## Motivation
To start, a human's main needs are food, clothing, and shelter. What separates food from the other two is the fact that one needs to make or buy food every single day, which is not the case for shelter and clothing. For something that must be prepared every single day (in this case, cooking), one would need availability in time and ingredients. Sometimes one has the time but not the ingredients, or vice-versa. This pushes me to making a recipe recommendation system. But, I myself have dietary limitations, and cannot seem to find the best recipe for myself. That is what motivated me to add a dietary preference feature.

## Web Scraping
BeautifulSoup was used to scrape more than 3000 recipes from [Jamie Oliver](https://www.jamieoliver.com/)
Recipe name, ingredients, difficulty, time needed, and url was extracted.

## Data Preprocessing
Ingredients were parsed in order to better filter the data. 
- Words were lemmatized (to ensure there is only one version of a word)
- Stop words were removed
- Measurements were removed
- Common ingredients were removed (we assume that every user has this ingredient available already, e.g. salt, pepper, etc.)
- NLP preprocessing were done: punctuation, accents, lowercase, etc.

## Model
The general idea is to use content-based filtering approach, enabling us to suggest recipes based on the ingredients provided by the user. To gauge the similarity between user-provided ingredients and recipes, I employed cosine similarity. The recommendation model calculates cosine similarity between the user-inputted ingredient list and all recipes in the corpus (specifically with the dietary restrictions). Subsequently, it outputs the top-n most similar recipes, allowing users to make their selections.
Continuous Bag of Words (CBOW) of Word2Vec neural network was used to create word embeddings for my collection of individual ingredients. This decision was made to accommodate textual representations to capture inherent similarities in word distributions. This allows commonalities between ingredients used together to be identified. 
To construct the recipe recommendation system, each ingredient list was condensed into a single embedding, to allow effective similarity calculation. TF-IDF aggregation of embeddings werre used to provide distinction between recipes by emphasizing unique ingredients.

## Deliverable
Streamlit was used to make a user-interactive [app](https://comfoodable.streamlit.app/)
The app sometimes needs to wake up before being available again. It might take some time.
The app also requires a few changes because of compatibility issues. Until it is fixed, screenshots are available to 
show the demo.






