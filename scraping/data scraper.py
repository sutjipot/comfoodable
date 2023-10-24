import pandas as pd
from bs4 import BeautifulSoup
import requests


# fetch html and beautiful soup parsing
#the url changes depending on what type of food is scraped. vegan (166), vegetarian(536), gluten free(1077), dairy free(319), and normal(1251)
url_vegan = "https://www.jamieoliver.com/recipes/category/course/quick-fixes/"

#other urls:
#https://www.jamieoliver.com/recipes/category/course/mains/
#https://www.jamieoliver.com/recipes/category/course/meals-for-one/
#https://www.jamieoliver.com/recipes/category/special-diets/vegetarian/
#https://www.jamieoliver.com/recipes/category/special-diets/vegan/
#https://www.jamieoliver.com/recipes/category/special-diets/gluten-free/
#https://www.jamieoliver.com/recipes/category/special-diets/dairy-free/

page = requests.get(url_vegan)
soup = BeautifulSoup(page.text, "html.parser")

# filter it to only get urls that contain recipes
recipe_url = pd.Series([a.get("href") for a in soup.find_all("a")])
recipe_url = recipe_url[(recipe_url.str.count("-") > 0) &
                        (recipe_url.str.contains("/recipes/") == True) &
                        (recipe_url.str.contains("-recipes/") == True) &
                        (recipe_url.str.contains("course") == False) &
                        (recipe_url.str.contains("books") == False) &
                        (recipe_url.str.endswith("recipes/") == False)].unique()

# store urls in df, make it a DataFrame
df = pd.DataFrame({"recipe_url": recipe_url})
df["recipe_url"] = "https://www.jamieoliver.com" + df["recipe_url"].astype("str")            

# specify the filename in the file path
df.to_csv(r"C:\Users\indir\OneDrive\Documents\Data\recipes.csv", sep="\t", index=False)


#when i want to add the recipe urls to an already existing file (adding extra recipes to mains)
#existing_df = pd.read_csv(r"C:\Users\indir\OneDrive\Documents\Data\mains url.csv")
#updated_df = existing_df._append(df, ignore_index=True)
#updated_df.to_csv(r"C:\Users\indir\OneDrive\Documents\Data\mains url.csv", index=False)
