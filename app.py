from flask import Flask, request, redirect
from flask import render_template
import api

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/recipe", methods = ['POST'])
def find_recipe():
    #code to find recipe
    recipes = api.get_recipe_from_ingredient(request.data)

    for i in recipes:
        ingredients = i["ingredients"]

        text = ""
        for j in ingredients:
            try:
                text += j + ", "
            except:
                print(j)
        
        text = text[:len(text) - 2] + "."

        i["ingredients"] = text

    return render_template("index.html", len = len(recipes), recipes = recipes)