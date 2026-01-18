from flask import Flask, render_template, request, redirect, url_for, session

# Flask initialization code
app = Flask(__name__)
app.secret_key = "TYPE-WITH-SPEED"

# Route for / as home page
@app.route("/")
def home():
    return render_template('index.html')


# The following command will start the backend in debug mode
# Debug mode se error dhond ne mea aasani hoti hy
if __name__ == "__main__":
    app.run(debug=True)
