# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# # app.config['SECRET_KEY'] = 'tester'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# class details(db.Model):  
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120),  nullable=False)
#     country = db.Column(db.String(120), nullable=False)
#     profession = db.Column(db.String(120), nullable=False)
#     hobby = db.Column(db.String(120))
#     def __repr__(self):
#         return {'id': self.id,
#         'name': self.name,
#         'email': self.email,
#         'hobby': self.hobby,
#         'country': self.country,
#         'profession': self.profession}
# @app.route('/info', methods =["GET", "POST"])
# def create():
#     return render_template("create.html")

# @app.route('/info/theme', methods =["GET", "POST"])
# def theme():
#     if request.method == "POST":
#         name = request.form['name']
#         email = request.form['email']
#         country = request.form['country']
#         profession = request.form['profession']
#         hobby = request.form['hobby']
#         try:
#             db.session.add(details(name= name,email = email,country= country, profession =profession,hobby= hobby))
#             db.session.commit()
#             print("Successfully added")
#             print(name, email, country, profession, hobby)
#             return redirect(url_for('theme'))
#         except:
#             return "There was an issue adding your details"
#     else:
#         return render_template('theme_select.html')


# if __name__ == '__main__':
#     app.run(debug=True, port=2322)
# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask import send_from_directory
# from datetime import datetime
# app = Flask(__name__)
# # app.config['SECRET_KEY'] = 'tester'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# class Details(db.Model):  
#     id = db.Column(db.Integer, primary_key=True);
#     name = db.Column(db.String(80));
#     email = db.Column(db.String(120));
#     country = db.Column(db.String(120));
#     profession = db.Column(db.String(120));
#     hobby = db.Column(db.String(120));
#     def __init__(self, name, email, country, profession, hobby):
#         self.name = name;
#         self.email = email;
#         self.country = country;
#         self.profession = profession;
#         self.hobby = hobby;
# @app.route('/info', methods =["GET", "POST"])
# def create():
#     if request.method == "POST":
#         name = request.form['name'];
#         email = request.form['email'];
#         country = request.form['country'];
#         profession = request.form['profession'];
#         hobby = request.form['hobby'];
#         db.session.add(Details(name, email, country, profession, hobby));
#         db.session.commit();
#         print(name, email, country, profession, hobby);
#         return redirect(url_for('theme'));
#     return render_template("create.html");

# @app.route('/info/theme', methods =["GET", "POST"])
# def theme():
#     return render_template("theme_select.html");


# @app.route('/result', methods=['POST','GET'])
# def result():
#     print(request.form)
#     result = Details.query.order_by(Details.id.desc()).first()
#     page = render_template('/black_theme/index.html', name=result.name, email=result.email, profession=result.profession, hobby=result.hobby, country=result.country)
#     filename = 'latest-' + datetime.now() + '.txt'
#     with open(filename, 'w') as f:
#         f.write(page)
#     return send_from_directory(
#         app.config['/static'], filename
#     )

# if __name__ == '__main__':
#     app.run(debug=True, port=2322)
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory
from datetime import datetime
import zipfile
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)
@app.route('/')
def index():
    return render_template('index.html')
class details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    country = db.Column(db.String(120))
    profession = db.Column(db.String(120))
    hobby = db.Column(db.String(120))
    youtube = db.Column(db.String(120))
    def __init__(self, name, email, country, profession, hobby, youtube):
        self.name = name
        self.email = email
        self.country = country
        self.profession = profession
        self.hobby = hobby
        self.youtube = youtube
@app.route('/info', methods =['GET','POST'])
def create():
    return render_template('create.html')
@app.route('/info/theme', methods =["GET", "POST"])
def theme():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        country = request.form['country']
        profession = request.form['profession']
        hobby = request.form['hobby']
        youtube = request.form['youtube']
        try:
            db.session.add(details(name= name,email = email,country= country, profession =profession,hobby= hobby, youtube = youtube))
            db.session.commit()
            print("Successfully added")
            print(name, email, country, profession, hobby, youtube)
            return redirect(url_for('theme'))
        except:
            return "There was an issue adding your details"
    else:
        return render_template('theme_select.html')

@app.route('/result', methods=["POST", "GET"])
def result():
    print(request.form)
    result = details.query.order_by(details.id.desc()).first()
    css_path = './static/black_theme/css/style.css'
    bg_img_path = './static/black_theme/css/img/bg.jpg'
    page = render_template('./black_theme/index.html', name=result.name, email=result.email, profession=result.profession, hobby=result.hobby, country=result.country,youtube=result.youtube, css_path = css_path, bg_img_path = bg_img_path)
    filename = 'black_theme.html'
    with open(filename, 'w') as f:
        f.write(page)
    with zipfile.ZipFile('black_theme.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        my_zip.write(filename)
        my_zip.write(css_path)
        my_zip.write(bg_img_path)
    return "Website Downloaded"
if __name__ == '__main__':
    app.run(debug=True, port=2322)