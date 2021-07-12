from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')
    
@app.route("/second_page")
def second_page():
    return render_template('about_page.html', subtitle='About Page', text='This is the about page')
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")