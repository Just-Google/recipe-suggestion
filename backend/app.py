from flask import Flask, request, redirect, send_file
from flask import render_template
import api
from mongo import Database

db = Database()
print("Mongodb is up")

app = Flask(__name__)
print("Server is up")

@app.route("/")
def index():
    return render_template("suggestion.html", len = 0, recipes = [])

@app.route("/App.css")
def css():
    return send_file("./templates/App.css")

@app.route("/recipe", methods = ['POST'])
def find_recipe():
    ing = request.form.get("ingredients")
    ing = ing.split(",")
    
    recipes = api.get_recipe_from_ingredient(ing, db)

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

    return render_template("suggestion.html", len = len(recipes), recipes = recipes)