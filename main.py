from flask import Flask, render_template, request
import requests
import smtplib

blogs_endpoint = "https://api.npoint.io/6813343cbd4fa3b4db51"
response = requests.get(blogs_endpoint)
json = response.json()

app = Flask(__name__)



MY_EMAIL = "testingtester983@gmail.com"
MY_PASSWORD = "cbjtqflmssyfuyzb"

@app.route('/')
def get_index():
    return render_template('index.html', data=json)

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/contact', methods=["POST", "GET"])
def get_contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)

@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for blog_post in json:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", blog=requested_post)

if __name__ == "__main__":
    app.run(debug=True)