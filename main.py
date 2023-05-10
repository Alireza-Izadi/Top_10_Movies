from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import EditForm, AddMovie

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap(app)


#Creating Database
db = SQLAlchemy(app)
class Movies(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year  = db.Column(db.Integer, nullable=False)
    description  = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'
    

app.app_context().push()
# db.create_all()

#Home Page
@app.route("/")
def home():
    all_movies = db.session.query(Movies).all()
    return render_template("index.html", movies = all_movies)

#Edit Movie Info
@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit_movie(id):
    form = EditForm()
    if form.validate_on_submit():
        movie_to_edit = Movies.query.get(id)
        movie_to_edit.rating = form.rating.data
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("edit.html", id=id, form=form)

#Add Movie
@app.route("/add", methods = ["POST", "GET"])
def add_movie():
    form = AddMovie()
    if form.validate_on_submit():
        new_movie = Movies(title= form.title.data, year= form.year.data, description= form.description.data, rating= form.rating.data, ranking= form.ranking.data, review= form.review.data, img_url= form.img_url.data)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form = form)

#Delete Movie
@app.route("/delete/<int:id>")
def delete_movie(id):
    movie_to_delete = Movies.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
