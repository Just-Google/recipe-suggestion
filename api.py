from bs4 import BeautifulSoup
import requests
import json
import threading

THREADCOUNT = 4

def get_recipe_multithread(db):
    pages = list(range(1, 72))
    thread = []
    while pages != []:
        for i in range(THREADCOUNT):
            if pages != []:
                num = pages.pop(0)
                thread.append(threading.Thread(target = get_recipe, args = (num, db, )))
        for i in thread:
            i.start()
        for i in thread:
            i.join()
        thread = []

def get_recipe(num, db):
    # Only work with this website currently
    print(f"Page {num} assigned to thread: {threading.current_thread().name}")
    r = requests.get('https://thewoksoflife.com/visual-recipe-index/page/' + str(num))
    r.close()

    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find("main", {"class": "content flexbox"}).find_all("a", {"class", "entry-image-link"})

    for i in result:
        link = i["href"]

        req = requests.get(link)

        recipe_html = req.text
        recipe_soup = BeautifulSoup(recipe_html, 'html.parser')

        recipe_soup = recipe_soup.find("div", {"class", "wprm-recipe-the-woks-of-life"})
        if recipe_soup == None:
            continue

        ing_list = []
        ing = recipe_soup.find_all("span", {"class", "wprm-recipe-ingredient-name"})
        for k in ing:
            if k.string != None:
                ing_list.append(k.string)

        title = recipe_soup.find("h2", {"class", "wprm-recipe-name wprm-block-text-normal"}).string

        pic = recipe_soup.find_all("img")[1]["src"]

        item = {"name": title, "ingredients": ing_list, "picture": pic, "link": link}

        db.insert(item)
        req.close()

def get_recipe_from_ingredient(js_data, db):
    data = json.loads(js_data)

    recipes = []

    for i in data["ingredients"]:
        result = db.get({"ingredients": i})
        for j in result:
            j.pop("_id")
            if j not in recipes:
                recipes.append(j)

    return recipes

