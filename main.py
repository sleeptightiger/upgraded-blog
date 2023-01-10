from flask import Flask, render_template
import requests
import pprint

blogs_endpoint = "https://api.npoint.io/6813343cbd4fa3b4db51"
response = requests.get(blogs_endpoint)
json = response.json()

app = Flask(__name__)

@app.route('/')
def get_index():
    return render_template('index.html', data=json)

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/contact')
def get_contact():
    return render_template('contact.html')

@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for blog_post in json:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", blog=requested_post)

if __name__ == "__main__":
    app.run(debug=True)