from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import scrape_mars

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_update = mongo.db.mars_update.find_one()
    return render_template("index.html", mars_update=mars_update)


@app.route("/scrape")
def scrape():
    mars_update = mongo.db.mars_update
    mars_update_data = scrape_mars.scrape()
    mars_update.update({}, mars_update_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)







