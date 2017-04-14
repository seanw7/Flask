from flask import Flask, render_template, session, redirect, request, url_for, g
from twitter_utils import get_request_token, get_oauth_verifier_url, get_access_token
from user import User
from database import Database

app = Flask(__name__)
app.secret_key = '1234'

Database.initialise(database='postgres', user='postgres', password='Ac3TeX411', host='localhost')

@app.before_request
def load_user():
    if 'screen_name' in session:
        g.user = User.load_from_db_by_screen_name(session['screen_name'])


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/login/twitter')
def twitter_login():
    if 'screen_name' in session:
        return redirect(url_for('profile'))
    request_token = get_request_token()
    session['request_token'] = request_token
    # to make sure twitter returns the proper pin code lets change the settings in our twitter 'app' for callback url!
    # sets the call back url to : "http://127.0.0.1:4995/auth/t witter"
    return redirect(get_oauth_verifier_url(request_token))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('homepage'))

@app.route('/auth/twitter') #  http://127.0.0.1:4995/auth/twitter?oauth_verifier=
def twitter_auth():
    oauth_verifier = request.args.get('oauth_verifier')
    access_token = get_access_token(session['request_token'], oauth_verifier)

    user = User.load_from_db_by_screen_name(access_token['screen_name'])
    if not user:
        user = User(access_token['screen_name'], access_token['oauth_token'],
                    access_token['oauth_token_secret'], None)
        user.save_to_db()
    # this will remember the users screen name with a cookie
    session['screen_name'] = user.screen_name
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return render_template('profile.html', user=g.user)



#app.run(debug=True)
app.run(port=4995)