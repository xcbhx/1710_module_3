# import flask library
from flask import Flask, request, render_template

import json

# set up app variable, to start writing routes
app = Flask(__name__)

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