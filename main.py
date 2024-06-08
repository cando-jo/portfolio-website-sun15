# Import
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)
# Tablo oluşturma

class Kullanici_bilgileri(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200), nullable=False)
    comment=db.Column(db.String(200), nullable=False)


with app.app_context():
    db.create_all()

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    email = request.form['email']
    comment = request.form['text']
    print("Email:", email)
    print("Comment:", comment)
    kullanici = Kullanici_bilgileri(email=email, comment=comment)
    
    db.session.add(kullanici)
    db.session.commit()
    
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(debug=True)

#github 1: https://github.com/cando-jo/sat-18-m7l2
#github (discord) 2:  https://github.com/cando-jo/ai-ve-discord
#github (microservices) 3: https://github.com/cando-jo/microservices-project
#github (web) 4:  https://github.com/cando-jo/web_tasarimi_ilk_ders
