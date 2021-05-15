from flask import Flask , render_template ,url_for , redirect ,request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('layout.html' , nadpis = "Home")

@app.route("/contact")
def sorry():
  return render_template('contact.html' , nadpis = "Sorry")

"""@app.route("/description")
def description():
  return render_template('description.html' , nadpis = "Description")"""
  
if __name__ == "__main__":
    app.run(debug=True , port=2451)
