from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('layout.html' , nadpis = "Home")

@app.route("/about")
def second_page():
  return render_template('second_page.html' , nadpis = "Home")

@app.route("/contact")
def contact():
  return render_template('contact.html' , nadpis = "Sorry")

  
if __name__ == "__main__":
    app.run(debug=True ,  host='0.0.0.0', port=3000)
