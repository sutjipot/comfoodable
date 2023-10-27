import pandas as pd
import nltk
import string
import ast
import re
import unidecode
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from collections import Counter


def ingredient_parser(ingredient):
    measurements = ["teaspoon", "t", "tsp.", "tsp", "tbsp", "tablespoon", "T", "tbl.", "tb", "tbsp.",
                "fluid ounce", "fl oz", "floz", "gill", "cup", "c", "pint", "p", "pt", "fl pt", "quart",
                "q", "qt", "fl qt", "gallon", "g", "gal", "ml", "milliliter", "millilitre", "cc", "ml",
                "mL", "l", "liter", "litre", "L", "dl", "dL", "deciliter", "decilitre", "bulb", "level",
                "heaped", "rounded", "whole", "bunch", "pinch", "medium", "slice", "pound", "lb", "#",
                "ounce", "oz", "mg", "milligram", "milligramme", "miligram", "g", "gram", "gramme", "kg",
                "kilogram", "kilogramme", "x", "of", "mm", "millimeter", "millimetre", "cm", "centimeter",
                "centimetre", "m", "meter", "metre", "inch", "in", "milli", "centi", "deci", "hecto", "kilo"]
    remove = ["fresh", "oil", "a", "red", "bunch", "and", "clove", "or", "leaf", "large", 
              "extra", "sprig", "ground", "handful", "free", "small", "pepper", "virgin", "range", "from", "dried",
              "sustainable", "black", "peeled", "higher", "welfare", "seed", "for", "finely", "freshly", "fine", "sea",
              "quality", "white", "ripe", "few", "piece", "source", "to", "organic", "flat", "smoked", "ginger", "sliced", 
              "green", "picked", "the", "stick", "plain", "plus", "mixed", "mint", "bay", "basil", "your", "cumin", 
              "optional", "fennel", "serve", "mustard", "unsalted", "baby", "paprika", "fat", "ask", "natural", "skin", 
              "roughly", "into", "such", "cut", "good", "brown", "grated", "trimmed", "oregano", "powder", "yellow", 
              "dusting", "knob", "frozen", "on", "deseeeded", "low", "runny", "balsamic", "cookeed", "streaky", "nutmeg", 
              "sage", "rasher", "zest", "pin", "groundnut", "breadcrumb", "turmeric", "halved", "grating", "stalk", "light", 
              "tinned", "dry", "soft", "rocket", "bone", "color", "colour", "washed", "skinless", "leftover", "splash", 
              "removed", "dijon", "thick", "big", "hot", "drained", "sized", "chestnut", "watercress", "fishmonger", "english", 
              "dill", "caper", "raw", "worcestershire", "flake", "cider", "cayenne", "leg", "pine", "wild", "if", "herb", 
              "almond", "shoulder", "cube", "dressing", "with", "chunk", "spice", "thumb", "garam", "new", "little", "punnet", 
              "peppercorn", "shelled", "saffron", "other", "chopped", "salt", "olive", "taste", "can", "sauce", "water", "diced", 
              "package", "italian", "shredded", "divided", "parsley", "vinegar", "all", "purpose", "all-purpose", "crushed", 
              "juice", "more", "coriander", "bell", "needed", "thinly", "boneless", "thumb", "half", "thyme", "cubed", 
              "cinnamon", "cilantro", "jar", "seasoning", "rosemary", "extract", "sweet", "baking", "beaten", "heavy", "seeded", 
              "tin", "vanilla", "uncooked", "crumb", "style", "thin", "nut", "coarsely", "spring",  "cornstarch", "strip", 
              "cardamom", "rinsed", "honey", "cherry", "root", "quartered", "head", "softened", "container", "crumble", "frying", 
              "lean", "cooking", "roasted", "warm", "whipping", "thawed", "pitted", "sun", "sun-dried", "kosher", "bite", 
              "toasted", "lasagna", "split", "melted", "degree", "lengthwise", "romano", "packed", "pod", "anchovy", "rom",
              "prepared", "juiced", "fluid", "floret", "room", "active", "seasoned", "mix", "deveined", "lightly", "anise", "thai", 
              "size", "unsweetened", "torn", "wedge", "sour", "basmati", "marinara", "dark", "temperature", "garnish", "bouillon", 
              "loaf", "shell", "reggiano", "canola", "parmigiano", "round", "canned", "ghee", "crust", "long", "broken", "ketchup", 
              "bulk", "cleaned", "condensed", "sherry", "provolone", "cold", "soda", "cottage", "spray", "tamarind", "pecorino", 
              "shortening", "part", "bottle", "sodium", "cocoa", "grain", "french", "roast", "stem", "link", "firm", "asafoetida", 
              "mild", "dash", "boiling", "instant", "strong", "sachet", "rack", "back"]
              
    #turn ingredient string to list
    if isinstance(ingredient, list):
        ingredients = ingredient
    else:
        ingredients = ast.literal_eval(ingredient) 

    #delete punctuation
    translator = str.maketrans("", "", string.punctuation)
    lemmatizer = WordNetLemmatizer()
    ingredients_list = []

    for i in ingredients:
        i.translate(translator)
        items = re.split(" |-", i) #split space, hyphens
        items = [word for word in items if word.isalpha()] #delete non alphabets
        items = [word.lower() for word in items] #all lowercase
        items = [unidecode.unidecode(word) for word in items] #delete accent
        items = [lemmatizer.lemmatize(word) for word in items] #lemmatize
        items = [word for word in items if word not in measurements] #delete measurements
        items = [word for word in items if word not in remove] #delete common words

        if items:
            ingredients_list.append(" ".join(items))
    
    return ingredients_list


#recipe_df changes for every file that we want to parse the ingredients of
#recipe_df = pd.read_csv(r"C:\Users\indir\OneDrive\Documents\Data\vegan full real.csv")
#recipe_df["parsed_ingredients"] = recipe_df["ingredients"].apply(lambda x: ingredient_parser(x))
#df = recipe_df[["name", "time", "difficulty", "ingredients", "parsed_ingredients", "recipe_url"]]
#df.to_csv(r"C:\Users\indir\OneDrive\Documents\Data\vegan parsed.csv", index=False)
    
