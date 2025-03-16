from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login('YOUR EMAIL', 'APP PASSWORD')
        server.sendmail(email, 'YOUR EMAIL', f"Subject: New Contact\n\n{name}: {message}")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)