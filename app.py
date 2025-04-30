from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/',methods=['GET','POSt'])
def index():
    password = " "
    if request.method == "POST":
        length = int(request.form['length'])
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        use_digits = 'digits' in request.form
        use_symbols = 'symbols' in request.form 
        characters = ''
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))
    return render_template('index.html',password= password)

    

if __name__ == '__main__':
    app.run(debug=True)
