from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    name = request.form.get('name')
    email = request.form.get('email')

    print(name, email)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()