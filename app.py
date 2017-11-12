import requests, json
from flask import Flask, request, render_template, send_from_directory
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    username="fe00ba2c-4f2e-43b8-8c51-88c15160f9cb",
    password="spYXrqwUwdiU",
    x_watson_learning_opt_out=True)  # Optional flag

jinjas_in_the_night = Flask(__name__)

@jinjas_in_the_night.route("/", methods = ["GET", "POST"])
def root():
    return render_template("template.html")

@jinjas_in_the_night.route("/listen", methods = ["POST"])
def listen():
	voice(request.form["user"])
	return send_from_directory("data", filename = "output.mp3")

def voice(text):
	with open(join(dirname(__file__), 'data/output.mp3'), 'wb') as audio_file:
		audio_file.write(text_to_speech.synthesize(text, accept='audio/mpeg', voice="en-US_AllisonVoice"))

if __name__ == "__main__":
    jinjas_in_the_night.debug = True
    jinjas_in_the_night.run()