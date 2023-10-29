from flask import Flask,render_template

app = Flask(__name__)

# NOTE : Test route for flask app
# @app.route("/")
# def index():
#     return True

@app.route("/")
def player_one():
    return render_template("player_one.html")

@app.route("/player_two",methods=["Get"])
def player_two():    
    return render_template("player_two.html")

@app.route("/player_three",methods=["Get"])
def player_three():    
    return render_template("player_three.html")

@app.route("/player_four",methods=["Get"])
def player_four():    
    return render_template("player_four.html")

@app.route("/player_five",methods=["Get"])
def player_five():    
    return render_template("player_five.html")

@app.route("/player_six",methods=["Get"])
def player_six():    
    return render_template("player_six.html")

@app.route("/player_seven",methods=["Get"])
def player_seven():    
    return render_template("player_seven.html")

@app.route("/player_eight",methods=["Get"])
def player_eight():    
    return render_template("player_eight.html")

@app.route("/player_nine",methods=["Get"])
def player_nine():    
    return render_template("player_nine.html")

@app.route("/player_ten",methods=["Get"])
def player_ten():    
    return render_template("player_ten.html")

@app.route("/player_eleven",methods=["Get"])
def player_eleven():    
    return render_template("player_eleven.html")

if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)