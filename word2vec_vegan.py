import unidecode
import ast
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from ingredientparser import ingredient_parser


def get_sort_corpus(data):
    sorted = []
    for i in data.parsed_ingredients.values:
        i.sort()
        sorted.append(i)
    return sorted

def parsetitle(title):
    return unidecode.unidecode(title)

def real_ingparse(ingredient):
    if isinstance(ingredient, list):
        ingreds = ingredient
    else:
        ingreds = ast.literal_eval(ingredient)
        
    ingreds = ",".join(ingreds)
    return unidecode.unidecode(ingreds)

def recommend(n, score):
    recipes = pd.read_csv("data/vegan parsed.csv")
    top = sorted(range(len(score)), key= lambda x: score[x], reverse= True)[:n]

    recommended = pd.DataFrame(columns=["recipe", "ingredients", "url", "time", "difficulty", "score"])
    count = 0
    for i in top:
        recipe_name = parsetitle(recipes.at[i, "name"])
        recommended.at[count, "recipe"] = recipe_name
        recommended.at[count, "ingredients"] = real_ingparse(recipes["ingredients"][i])
        recommended.at[count, "url"] = recipes["recipe_url"][i]
        recommended.at[count, "score"] = f"{score[i]}"
        recommended.at[count, "time"] = recipes["time"][i]
        recommended.at[count, "difficulty"] = recipes["difficulty"][i]
        count += 1
    return recommended

class MEV(object):
    def __init__(self, wordmodel):
        self.wordmodel = wordmodel
        self.vecsize = wordmodel.wv.vector_size

    def fit(self):
        return self
    
    def word_avg_list(self, docs):
        return np.vstack([self.word_avg(sent) for sent in docs])

    def word_avg(self, sent):
        mean = []
        for i in sent:
            if i in self.wordmodel.wv.index_to_key:
                mean.append(self.wordmodel.wv.get_vector(i))
        
        if not mean:
            return np.zeros(self.vecsize)
        else:
            return np.array(mean).mean(axis=0)


    def transform(self, docs):
        return self.word_avg_list(docs)
    

class TFIDFvectorizer(object):
    def __init__(self, wordmodel):
        self.wordmodel = wordmodel
        self.word_idf_weight = None
        self.vecsize = wordmodel.wv.vector_size

    def fit(self, docs):
        text_docs = []
        for doc in docs:
            text_docs.append(" ".join(doc))

        tfidf = TfidfVectorizer()
        tfidf.fit(text_docs)

        max_idf = max(tfidf.idf_)
        self.word_idf_weight = defaultdict(lambda: max_idf, [(word, tfidf.idf_[i]) for word, i in tfidf.vocabulary_.items()])
        return self
    
    def word_avg(self, sent):
        mean = []
        for word in sent:
            if word in self.wordmodel.wv.index_to_key:
                mean.append(self.wordmodel.wv.get_vector(word)*self.word_idf_weight[word])
        
        if not mean:
            return np.zeros(self.vecsize)
        else:
            return np.array(mean).mean(axis=0)
        
    def word_avg_list(self, docs):
        return np.vstack([self.word_avg(sent) for sent in docs])
        
    def transform(self, docs):
        return self.word_avg_list(docs)

def get_vegan_recs(ingredients, n=10, mean=False):
    model = Word2Vec.load("model_cbow.bin")
    model.init_sims(replace=True)
    if model:
        print("success")
    
    data = pd.read_csv("data/vegan parsed.csv")
    data["parsed_ingredients"] = data.ingredients.apply(ingredient_parser)
    corpus = get_sort_corpus(data)

    if mean:
        mean_vec = MEV(model)
        doc_vec = mean_vec.transform(corpus)
        doc_vec = [doc.reshape(1,-1) for doc in doc_vec]
        assert len(doc_vec) == len(corpus)

    else:
        tfidf_vec = TFIDFvectorizer(model)
        tfidf_vec.fit(corpus)
        doc_vec = tfidf_vec.transform(corpus)
        doc_vec = [doc.reshape(1,-1) for doc in doc_vec]
        assert len(doc_vec) == len(corpus)

    input = ingredients
    input = input.split(",")
    input = ingredient_parser(input)

    if mean:
        input_embed = mean_vec.transform([input])[0].reshape(1,-1)
    else:
        input_embed = tfidf_vec.transform([input])[0].reshape(1,-1)

    cosine_sim = map(lambda x: cosine_similarity(input_embed, x)[0][0], doc_vec)
    score = list(cosine_sim)
    return recommend(n, score)


#example run
#input = "garlic, rice noodle, tofu"
#rec = get_vegan_recs(input)
#print(rec)


    
