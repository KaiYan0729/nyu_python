from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import time
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

#reference
#https://pythonspot.com/en/login-authentication-with-flask/
@app.route('/')
def index():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
	if request.form['password'] == '1234' and request.form['username'] == 'kai':
		session['logged_in'] = True
		#return posts()
	else:
		flash('wrong password!')
		time.sleep(3)
	return redirect("/")

#reference
#https://pythonspot.com/en/login-authentication-with-flask/
#http://www.jamesharding.ca/posts/simple-static-markdown-blog-in-flask/
@app.route ('/posts')
def posts():
	if session.get('logged_in'):
		posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
		posts.sort(key=lambda item:item['date'], reverse=True)
		return render_template('posts.html', posts=posts)
	else:
		return index()

@app.route('/posts/<name>/')
def post(name):
	path = '{}/{}'.format(POST_DIR, name)
	post = flatpages.get_or_404(path)
	return render_template('post.html', post=post)


@app.route("/logout")
def logout():
	session['logged_in'] = False
	return index()

if __name__=="__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True)
