import os
from flask import Flask, flash, render_template, redirect, request, url_for, session
import json 
from bson import json_util
from bson.json_util import dumps
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'some_secret' 
app.config["MONGO_DBNAME"] = 'myrecipe'
app.config["MONGO_URI"] ='mongodb://root:Rovrec1@ds119220.mlab.com:19220/myrecipe'

mongo = PyMongo(app)

#....LANDING PAGE 

@app.route('/')
def index():
    return render_template('index.html')


#....GET SEASON CATEGORIES...provides username based on user input
   
@app.route('/get_seasons', methods=["GET","POST"])
def get_seasons():
    if request.method == "POST":
        username = request.form["username"]
        session["user"] = username
        return render_template('seasons.html')
    return redirect(url_for('seasons'))  

# SEASON PAGE 

@app.route('/seasons')
def seasons():
    return render_template('seasons.html')
    
#....FINDS ALL RECIPES IN DATABASE & DISPLAYS THEM ON PAGE TO USER 

@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html',
    recipes=mongo.db.recipes.find({ '$query': {}, '$orderby': { '_id' : -1 } }))
    
# ....FILTERS SUMMER SMOOTHIE RECIPES 

@app.route('/get_summer')
def get_summer():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find({"season" : "summer"}))

 
# ......FILTERS AUTUMN SMOOTHIE RECIPES 

@app.route('/get_autumn')
def get_autumn():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find({"season" : "autumn"}))

# ......FILTERS SPRING SMOOTHIE RECIPES 

@app.route('/get_spring')
def get_spring():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find({"season" : "spring"}))
    
# ......FILTERS WINTER SMOOTHIE RECIPES 

@app.route('/get_winter')
def get_winter():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find({"season" : "winter"}))



# ......SEARCH RECIPES BY ALLERGEN

@app.route('/search_dairyfree')
def search_dairyfree():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find({"dietary_requirement_type": "dairy-free"}))
    
@app.route('/search_glutenfree')
def search_glutenfree():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find({"dietary_requirement_type": "gluten-free"}))

@app.route('/search_nutfree')
def search_nutfree():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find({"dietary_requirement_type": "nut-free"}))
    
@app.route('/search_vegan')
def search_vegan():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find({"dietary_requirement_type": "vegan"}))



#....... SEARCH RECIPES BY DIFFICULTY

@app.route('/search_easypeas')
def search_easypeas():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find({"difficulty_rating": "easy peas"}))
        
@app.route('/search_someeffort')
def search_someeffort():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find({"difficulty_rating": "some effort"}))

@app.route('/search_worthfaff')
def search_worthfaff():
    return render_template('search-results.html',
        recipes=mongo.db.recipes.find({"difficulty_rating": "worth all the faff"}))

#..... SEARCH RECIPES BY POPULARITY / STAR RATING 

@app.route('/search_popular')
def search_popular():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find( { '$query': {}, '$orderby': { 'star_rating_value' : -1 } } ))

@app.route('/search_leastpopular')
def search_leastpopular():
    return render_template('search-results.html',
    recipes=mongo.db.recipes.find( { '$query': {}, '$orderby': { 'star_rating_value' : 1 } } ))    

#....DISPLAYS ADD RECIPE PAGE 

@app.route('/add_recipe')
def add_recipe():
    return render_template('add-recipe.html',
    seasons=mongo.db.seasons.find(),
    difficulty_rating=mongo.db.difficulty_rating.find(),
    dietary_requirements=mongo.db.dietary_requirements.find(),
    star_rating=mongo.db.star_rating.find())


#....INSERTS RECIPE INTO DATABASE

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipe=mongo.db.recipes
    ingreds_req=request.form.getlist('ingredients')
    method_steps=request.form.getlist('method')
    method_steps_no_blanks = [i for i in method_steps if i != ""]
    diet_req=request.form.getlist('dietary_requirement_type')
    recipe_details = {
        'name_of_recipe':request.form['name_of_recipe'],
        'author':request.form['author'],
        'serves': request.form['serves'],
        'time_taken': request.form['time_taken'],
        'season':request.form['season'],
        'difficulty_rating':request.form['difficulty_rating'],
        'ingredients': ingreds_req,
        'method':method_steps_no_blanks,
        'star_rating_value':request.form['star_rating_value'],
        'dietary_requirement_type':diet_req
    }
    recipe.insert_one(recipe_details)
    return redirect(url_for('get_recipes'))

# ........EDIT RECIPE, DISPLAYS SELECTED RECIPE

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_seasons=mongo.db.seasons.find()
    seasons_list=[season for season in all_seasons]
    
    all_difficulties=mongo.db.difficulty_rating.find()
    difficulty_list=[difficulty for difficulty in all_difficulties]
    
    all_diet_reqs=mongo.db.dietary_requirements.find()
    diet_req_list=[diet for diet in all_diet_reqs]
    
    all_star_rating=mongo.db.star_rating.find()
    star_rating_list=[star for star in all_star_rating]
    
    return render_template('edit-recipe.html', 
                            recipe=the_recipe, 
                            seasons=seasons_list, 
                            difficulty_rating=difficulty_list,
                            star_rating=star_rating_list,
                            dietary_requirements=diet_req_list)
                            
# .........UPDATES RECIPE   

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    ingreds=request.form.getlist('ingredients')
    method_steps=request.form.getlist('method')
    method_steps_no_blanks = [i for i in method_steps if i != ""]
    diet_req=request.form.getlist('dietary_requirement_type')
    recipe.update_one( {'_id': ObjectId(recipe_id)}, 
    {'$set':
        {
            'name_of_recipe':request.form['name_of_recipe'],
            'author':request.form['author'],
            'serves': request.form['serves'],
            'time_taken': request.form['time_taken'],
            'season':request.form['season'],
            'difficulty_rating':request.form['difficulty_rating'],
            'ingredients': ingreds,
            'method': method_steps_no_blanks,
            'star_rating_value':request.form['star_rating_value'],
            'dietary_requirement_type':diet_req
        }
    })
    return redirect(url_for('get_recipes'))
    
# ....................DELETES RECIPE

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    flash("DELETED! (Caution: please remember this action is permanent!)")
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    
# ................DIETARY REQ CHART -shows user number of recipes that are eg nut free etc
    
@app.route('/pie_chart')
def pie_chart():
    
    recipes=mongo.db.recipes.find()
    data = {}
    
    for recipe in recipes:
        
        for diet in recipe.get('dietary_requirement_type',[]):
            starting_count = data.get(diet,0)
            data[diet] = starting_count + 1
            
    data_labels = []
    data_values = []
    
    for k,v in data.items():
        data_labels.append(k)
        data_values.append(v)
        
    print("data_labels",json.dumps(data_labels), json.dumps(data_values))
    return render_template('graph.html', data_labels=json.dumps(data_labels), data_values=json.dumps(data_values))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)