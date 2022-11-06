from flask import Flask, request, redirect
from flask import render_template
import api
from mongo import Database

db = Database()
print("Mongodb is up")

app = Flask(__name__)
print("Server is up")

@app.route("/")
def index():
    return render_template("index.html", len = 0, recipes = [])

@app.route("/recipe", methods = ['POST'])
def find_recipe():
    recipes = api.get_recipe_from_ingredient(request.data, db)

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