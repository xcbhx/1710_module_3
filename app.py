# import flask library
from flask import Flask, request, render_template
from flask_pymongo import PyMongo
import json

# set up app variable, to start writing routes
app = Flask(__name__)

# Create a configuration variable that utilizes my connections string!
app.config["MONGO_URI"] = "mongodb+srv://ceinaellison:ZLLWCMQ4Guw1EJPY@cluster0.qrgzj.mongodb.net/1710_module_3?retryWrites=true&w=majority&appName=Cluster0"

# C.R.U.D. = Create, Read, Update, Delete
mongo = PyMongo(app)

# CREATE
new_user = {
    'first_name': 'Ceina',
    'role': 'student',
    'course': '1710'
}
# print("Mongo ***")
# print(mongo)
# print("Mongo DB **")
# print(mongo.db)

# print("Results **")
result = mongo.db.users.insert_one(new_user)
# print(result)
# print("****")

# Reading all documents in a collection and printing the results
all_users = mongo.db.users.find()
for user in all_users:
    print(user['first_name'])

# Reading documents that have a 'course' of '1710'
all_students = mongo.db.users.find({'course': '1710'})
for user in all_students:
    print(user['first_name']) 

# UPDATE | Finding a document and updating it with changes
searchParam = { 'first_name': 'Ceina'}
changes = {'$set': {'course': '1111' }}
user = mongo.db.users.update_one(searchParam, changes)

# DELETE | Removing the document with a 'first_name' of 'Ceina' from the users collection
result = mongo.db.users.delete_one({
    'first_name': 'Ceina'
})
print(result.deleted_count)

@app.route('/')
def displayHomepage():
    return render_template('index.html')

@app.route('/formExample')
def firstForm():
    return render_template('form.html')

@app.route('/results', methods=['GET'])
def simple_pizza_results():

    # A context object contains all of the needed form data for the template
    context = {
        'pizza_flavor': request.args.get("pizza_flavor"),
        'crust': request.args.get("crust"),
        'individual_toppings': ['mushrooms', 'olives', 'garlic']
    }

    return render_template('confirmation_page.html', **context)

with open('exampleObj.json') as example_obj_file:
    print('raw file printed = ', example_obj_file)
    jsonData = json.load(example_obj_file)
    print('just the JSON data printed = ', jsonData)

@app.route('/jsonExample', methods=['GET'])
def jsonRoute():
    return jsonData


if __name__ == '__main__':
    app.run(port=8000, debug=True)