import pandas as pd 
import requests
import time
from bs4 import BeautifulSoup
import numpy as np


#scrape recipe details: url, name, ingredients, time, difficulty, labels
class ClassParse():
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(url).content, "html.parser")

    def name(self):
        try:
            return self.soup.find("h1").text.strip()
        except:
            return np.nan
        
    def time(self):
        try:
            return self.soup.find('div', {'class': 'recipe-detail time'}).text.split('In')[1]
        except:
            return np.nan
        
    def difficulty(self):
        try:
           return self.soup.find('div', {'class': 'col-md-12 recipe-details-col remove-left-col-padding-md'}).text.split('Difficulty')[1]
        except:
            return np.nan
        
    def ingredients(self):
        try:
            ingredients = []
            for li in self.soup.select(".ingred-list li"):
                ingred = " ".join(li.text.split())
                ingredients.append(ingred)
            return ingredients
        except:
            return np.nan

    

#read url csvs. there are mains, vegan, vegetarian, gluten-free, and dairy-free csvs.
recipe_df = pd.read_csv(r"C:\Users\indir\OneDrive\Documents\Data\mains url.csv")
attribute = ["name", "time", "difficulty", "ingredients"]

temp = pd.DataFrame(columns=attribute)
for i in range(00, len(recipe_df["recipe_url"])):
    url = recipe_df["recipe_url"][i]
    scraper = ClassParse(url)
    temp.loc[i] = [getattr(scraper, attrib)() for attrib in attribute]
    if i % 25 == 0:
        print(f"step {i} complete")
    time.sleep(np.random.randint(1,4))

temp["recipe_url"] = recipe_df["recipe_url"]
columns = ["recipe_url"] + attribute
temp = temp[columns]

dairyfree_df = temp
dairyfree_df.to_csv(r"C:\Users\indir\OneDrive\Documents\Data\mains full real.csv", index=False)

