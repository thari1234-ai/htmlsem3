from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def form():
   
    return render_template_string(open("11th june.html").read())

@app.route('/submit', methods=["POST"])
def submit():
    name = request.form.get('fname')
    if not name:
        return "Name can't be empty!"
    return f"Hi, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
