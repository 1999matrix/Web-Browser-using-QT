from flask import Flask , render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://big87505:Big123@cluster0.guf6zic.mongodb.net/?retryWrites=true&w=majority"
db = PyMongo(app).db
 
@app.route('/add', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        idnt = request.form['id']

        # Save the data to MongoDB
        data = {
            'name': name,
            'college': college,
            'id' : idnt
        }
        db.users.insert_one(data)

    return render_template('index.html')

@app.route('/students')
def users():
    # Get all the users from MongoDB
    users = db.Cluster0.find()

    return render_template('show_data.html', users=users)


if __name__ == '__main__':
    app.run(debug=True , port = 5001)