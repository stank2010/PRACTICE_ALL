from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

# use session , methods(GET and POST)
# Edite from https://flask.palletsprojects.com/en/1.0.x/quickstart/#what-to-do-if-the-server-does-not-start

app.secret_key = 'stankishere'

@app.route('/')
def index():
    if 'username' in session:
        return '''
            Logged in as %s <br>
            <form method="post" action="/logout">
                <p><input type=submit value=Logout>
            </form>
            '''%escape(session['username'])
    return 'You are not logged in <br> <button><a href="/login">login</a></button>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    if request.method == 'POST':
        session.pop('username', None)
        return redirect(url_for('index'))
