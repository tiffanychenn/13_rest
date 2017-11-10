import requests, json
from flask import Flask, render_template

link = "https://api.nasa.gov/planetary/apod?api_key=nvBh1FmpyC4jlCwklqCtpLrajtWXclmokLU5A6pd"
r = requests.get(link)		#make the API call
data = r.json()				#convert to a json object

jinjas_in_the_night = Flask(__name__)

@jinjas_in_the_night.route("/")
def root():
    return render_template("template.html", pic_title = data["title"], image = data["url"], info = data["explanation"])

if __name__ == "__main__":
    jinjas_in_the_night.debug = True
    jinjas_in_the_night.run()