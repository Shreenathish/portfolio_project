from flask import Flask, jsonify, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Select, String, Boolean
from random import choice
from flask_wtf import FlaskForm 
from wtforms import StringField,BooleanField ,SubmitField,IntegerField
from wtforms.validators import DataRequired,URL
from smtplib import SMTP

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:\portfolio_project\cafe-wifi-web\instance\cafes.db'
app.config['SECRET_KEY'] = 'shreenathish'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

class form(FlaskForm):
    name = StringField("Name")
    map_url = StringField('Map URL', validators=[DataRequired(), URL()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('Seats', validators=[DataRequired()])
    has_toilet = BooleanField('Has Toilet')
    has_wifi = BooleanField('Has Wi-Fi')
    has_sockets = BooleanField('Has Sockets')
    can_take_calls = BooleanField('Can Take Calls')
    coffee_price = StringField('Coffee Price')
    submit = SubmitField('Submit')

class updateform(FlaskForm):
    seats = StringField('Seats', validators=[DataRequired()])
    has_toilet = BooleanField('Has Toilet')
    has_wifi = BooleanField('Has Wi-Fi')
    has_sockets = BooleanField('Has Sockets')
    can_take_calls = BooleanField('Can Take Calls')
    coffee_price = StringField('Coffee Price')
    submit = SubmitField('Submit')


    
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"]) 
def get_the_cafe():
    result = db.session.execute(Select(Cafe))
    all_cafe = result.scalars().all()
    if not all_cafe:
        return jsonify({"error": "No cafes found"}), 404
    random_cafe = choice(all_cafe)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })

@app.route('/add',methods = ['GET','POST'])
def add_cafes():
    forms = form()
    if forms.validate_on_submit():
        name = forms.name.data
        map_url = forms.map_url.data
        img_url = forms.img_url.data
        location = forms.location.data
        seats = forms.seats.data
        has_toilet = forms.has_toilet.data
        has_wifi = forms.has_wifi.data
        has_sockets = forms.has_sockets.data
        can_take_calls = forms.can_take_calls.data
        coffee_price = forms.coffee_price.data
        new_cafe = Cafe(
            name=name,
            map_url=map_url,
            img_url=img_url,
            location=location,
            seats=seats,
            has_toilet=has_toilet,
            has_wifi=has_wifi,
            has_sockets=has_sockets,
            can_take_calls=can_take_calls,
            coffee_price=coffee_price
        )

        db.session.add(new_cafe)
        db.session.commit()
        return render_template('index.html')
    return render_template('add.html',forms = forms)
    
        
@app.route('/view',methods = ['GET','POST'])
def view():
    if request.method == 'GET':
        result = db.session.execute(Select(Cafe)).scalars().all()
    return render_template('view.html',form = result)

@app.route('/delete')
def delete():
    id = request.args.get("id")
    delete = db.get_or_404(Cafe,id)
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for("view"))

@app.route('/update',methods = ['GET','POST'])
def update():
    forms = updateform()
    id = request.args.get("id")
    update = db.get_or_404(Cafe,id)
    if forms.validate_on_submit():
        update.seats = forms.seats.data
        update.has_toilet = forms.has_toilet.data
        update.has_wifi = forms.has_wifi.data
        update.has_sockets = forms.has_sockets.data
        update.can_take_calls = forms.can_take_calls.data
        update.coffee_price = forms.coffee_price.data
        db.session.commit()
        return redirect(url_for('view'))
    return render_template('update.html',forms = forms,update = update)

@app.route('/order')
def order():
    id = request.args.get("id")
    order = db.get_or_404(Cafe, id)
    name = order.name
    seat = order.seats
    price = order.coffee_price
    email = 'nathishred@gmail.com'
    password = 'kvwefaijhxgnwslb'
    
    msg = f'Subject: Your order placed.\n\nName: {name}\nSeats: {seat}\nPrice: {price}'

    connect = SMTP('smtp.gmail.com', 587)
    connect.starttls()
    connect.login(user=email, password=password)
    connect.sendmail(from_addr=email, to_addrs=email, msg=msg.encode('utf-8'))
    connect.close()
    
    db.session.commit()
    return redirect(url_for('view'))

if __name__ == '__main__':
    app.run(debug=True)
