from flask import Flask,jsonify
import os
import openai
from flask import render_template


app = Flask(__name__)


apikey = "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"

@app.route("/")
def hello():
    return render_template('index.html',)


@app.route("/generateImages/<prompt>")
def generate(prompt):
    print("prompt",prompt)
    openai.api_key = apikey
    response = openai.Image.create(prompt=prompt, n=5, size="256x256") 
    print(response)
    return jsonify(response)




if __name__ == "__main__":
    app.run(port=8888)