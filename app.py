from flask import Flask, render_template, request, redirect, url_for, session

# Flask initialization code
app = Flask(__name__)
app.secret_key = "TYPE-WITH-SPEED"

# Route for / as home page
@app.route("/")
def home():
    # Fetching high score from session
    best_acc = session.get('best_acc') or 0
    best_wpm = session.get('best_wpm') or 0

    return render_template(
        'home.html',
        best_acc = best_acc,
        best_wpm = best_wpm
    )

# Route for typing speedtest page
@app.route("/typing-speedtest")
def speedtest():
    return render_template('speedtest.html')

# Route for saving best score
@app.route("/update/best/score", methods=["POST"])
def udpate_best_score():
    # Checking previous data of best score
    best_acc = session.get('best_acc') or 0
    best_wpm = session.get('best_wpm') or 0

    try:
        acc = int(request.form['acc'])
        wpm = int(request.form['wpm'])
        
        # Checking if current score is best or not
        if (wpm > best_wpm):
            best_wpm = wpm
            best_acc = acc

        # Saving best scores in session
        session['best_acc'] = best_acc
        session['best_wpm'] = best_wpm

    except:
        return 'error'

    return 'success'

# The following command will start the backend in debug mode
# Debug mode se error dhond ne mea aasani hoti hy
if __name__ == "__main__":
    app.run(debug=True)
