from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates1")  # make sure folder name matches

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('success', name=name, email=email, password=password))
    return render_template("form1.html")
  # this must match the HTML filename

@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('password')
    return f"<h2>Success!</h2><p>Name: {name}</p><p>Email: {email}</p><p>Password: {password}</p>"

if __name__ == '__main__':
    app.run(debug=True)
