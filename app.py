import collections
from flask import Flask, redirect, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)

db = client.Pride
collection = db.data

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = collection.find({
            'city': request.form['city']
        })
        # data = addData.query.order_by(addData.name).all()
        return render_template('index.html', data=data)
    else:
        data = ""
        return render_template('index.html', data=data)

@app.route('/add', methods=['POST', 'GET'])
def add():    
    if request.method == 'POST':               
            cbOpening = request.form.getlist('cbOpening')
            cbOpeningSpecialArea = request.form.getlist('cbOpeningSpecialArea')
            cbRoute = request.form.getlist('cbRoute')
            cbClosing = request.form.getlist('cbClosing')
            cbClosingSpcialArea = request.form.getlist('cbClosingSpcialArea')
            collection.insert_one({
                'city': request.form['city'],
                'date': request.form['date'],
                'time': request.form['time'],
                'place': request.form['place'],
                'phone': request.form['phone'],
                'email': request.form['email'],
                'name': request.form['name'],
                'opening_comments': request.form['opening_comments'],
                'closing_comments': request.form['closing_comments'],
                'route_comments': request.form['route_comments'],
                'openingOther': request.form['openingOther'],
                'openingSpcialAreaOther': request.form['closingOther'],
                'closingSpcialAreaOther': request.form['closingSpcialAreaOther'],
                'closingOther': request.form['closingOther'],
                'routeOther': request.form['routeOther'],                                
                'cbOpening': cbOpening,
                'cbOpeningSpecialArea': cbOpeningSpecialArea,
                'cbRoute': cbRoute,
                'cbClosing': cbClosing,
                'cbClosingSpcialArea': cbClosingSpcialArea
            })
            return redirect('/')

    else:
        return render_template('add.html')
if __name__ == "__main__":
    app.run(debug=True)