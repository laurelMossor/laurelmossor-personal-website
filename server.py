from flask import Flask, redirect, render_template, flash


app = Flask(__name__)
# app.secret_key = os.environ['FLASK_SECRET_KEY'] 
app.secret_key = "dev" # TODO: When in production, change to the above, and source secrets


@app.route("/")
def homepage():

    return render_template("homepage.html")




###########################################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # In debug mode, page will be updated when code is changed, change to debug=True/False