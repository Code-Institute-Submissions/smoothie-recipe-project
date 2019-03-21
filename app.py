import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myrecipe'
app.config["MONGO_URI"] ='mongodb://root:Rovrec1@ds119220.mlab.com:19220/myrecipe'

mongo = PyMongo(app)

#....HOME PAGE 

@app.route('/')
def index():
    return render_template('index.html')

#....GET SEASON CATEGORIES
   
@app.route('/get_seasons')
def get_seasons():
    return render_template('seasons.html')
    
#....FINDS ALL RECIPES IN DATABASE & DISPLAYS THEM ON PAGE 

@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html',
    recipes=mongo.db.recipes.find())
    
# FILTER SUMMER SMOOTHIES  

@app.route('/get_summer')
def get_summer():
    return render_template('results.html',
    recipes=mongo.db.recipes.find({"season" : "summer"}))

# FILTER SUMMER SMOOTHIES  

@app.route('/get_winter')
def get_winter():
    return render_template('results.html',
    recipes=mongo.db.recipes.find({"season" : "winter"}))
    
@app.route('/recipes_by_season/<season>', methods=["POST"])
def recipes_by_season(season):
    """
    Get all recipes of a chosen category and display
    these recipes on one page
    """
    # Counts total amount of chosen category recipes
    recipes_total = mongo.db.recipes.find({
        "season": season
    }).count()
    return render_template(
        "results.html",
        recipes=mongo.db.recipes.find({"season": season}),
        recipe=mongo.db.recipes.find(),
        season=season,
        recipes_total=recipes_total)
        


#....DISPLAYS ADD RECIPE PAGE ...............

@app.route('/add_recipe')
def add_recipe():
    return render_template('add-recipe.html',
    seasons=mongo.db.seasons.find(),
    difficulty_rating=mongo.db.difficulty_rating.find(),
    dietary_requirements=mongo.db.dietary_requirements.find(),
    star_rating=mongo.db.star_rating.find())

# ....SEARCH PAGE........................

@app.route('/search')
def search():
    return render_template('search-recipe.html', recipe=mongo.db.recipe.find(), seasons=mongo.db.seasons.find(),
    difficulty_rating=mongo.db.difficulty_rating.find(),
    dietary_requirements=mongo.db.dietary_requirements.find(),
    star_rating=mongo.db.star_rating.find())


#....SEARCH season FILTER FUNCTION
# @app.route('/search_winter')
# def search_winter():
#     the_recipe=mongo.db.recipes.find({"season": "winter"})
#     return render_template('results.html', recipe=the_recipe)

# @app.route('/search_result', methods=['GET', 'POST'])
# def search_result():
#     search_term = []
#     if request.method == 'POST':
#         search_term = request.form['ingredients']
#     return render_template('results.html', the_recipe=mongo.db.the_recipes.find_one({"ingredients": search_term}))
    
#....SEARCH FILTER FUNCTION


# @app.route('/search_result/<recipe_id>', methods=["GET"])
# def search_result(recipe_id):
#     recipe=mongo.db.recipes
#     recipe.find( { "ingredients": "almond" } )

#     # recipe.find( {'_id': ObjectId(recipe_id)},
#     # {
#     #     'author':request.form.get['author'],
#     #     'season':request.form.get['season']})
#     return redirect(url_for('get_recipes'))

#....INSERTS IN TO DATABASE..............

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipe=mongo.db.recipes
    ingreds=request.form.getlist('ingredients')
    method_steps=request.form.getlist('method')
    diet_req=request.form.getlist('dietary_requirement_type')
    recipe_details = {
        'name_of_recipe':request.form['name_of_recipe'],
        'author':request.form['author'],
        'serves': request.form['serves'],
        'time_taken': request.form['time_taken'],
        'season':request.form['season'],
        'difficulty_rating':request.form['difficulty_rating'],
        'ingredients': ingreds,
        'method':method_steps,
        'star_rating_value':request.form['star_rating_value'],
        'dietary_requirement_type':diet_req
    }
    recipe.insert_one(recipe_details)
    return redirect(url_for('get_recipes'))

# EDIT RECIPE, DISPLAYS SELECTED RECIPE

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
# UPDATES RECIPE   

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    ingreds=request.form.getlist('ingredients')
    method_steps=request.form.getlist('method')
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
            'method': method_steps,
            'star_rating_value':request.form['star_rating_value'],
            'dietary_requirement_type':diet_req
        }
    })
    return redirect(url_for('get_recipes'))
    
# ........DELETES RECIPE..............

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)