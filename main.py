# Import
from flask import Flask, render_template,request, redirect

app = Flask(__name__)

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
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(debug=True)

#github 1: https://github.com/cando-jo/sat-18-m7l2
#github (discord) 2:  https://github.com/cando-jo/ai-ve-discord
#github (microservices) 3: https://github.com/cando-jo/microservices-project
#github (web) 4:  https://github.com/cando-jo/web_tasarimi_ilk_ders
