from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()



my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_EMAIL_PASSWORD")
add = os.environ.get("TO_EMAIL")


def send_email(name, email, phone, message):
    email_message = f"""subject: new contact form submission
Name: {name}
Email: {email}
Phone: {phone}
message: {message}"""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=add, msg=email_message)


app = Flask(__name__)


@app.route("/")
def home():
    posts = requests.get(url="https://api.npoint.io/942799dc38830dbaaba3").json()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    posts = requests.get(url="https://api.npoint.io/942799dc38830dbaaba3").json()
    requested_post = next((post for post in posts if post["id"] == post_id), None)
    return render_template("post.html", post=requested_post)


@app.route("/from-entry", methods=["POST"])
def submit_form():
    data = request.form
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    message = data.get("message")

    send_email(name, email, phone, message)

    return "<h1>Successfully sent your message</h1>"


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
