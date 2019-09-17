# Pig Latinizer
# https://hidden-journey-62459.herokuapp.com/
# Request URL = https://hidden-journey-62459.herokuapp.com/piglatinize/
# Response Header = Location
# Request Method = POST

import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def pig_latinize(fact):

    payload = {'input_text': fact}
    response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/",
                             data=payload, allow_redirects=False)
    return response.headers['Location']

@app.route('/')
def home():
    fact = get_fact()
    latinized = pig_latinize(fact)

    page = f'<a href="{latinized}">{latinized}</a>'
    return page
    #return latinized

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
