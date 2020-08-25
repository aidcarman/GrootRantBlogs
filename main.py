from flask import Flask, render_template, request
from random import choice
import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyAHF0boQBojwlaGKfeHlFy_VOtquOr0aqM",
  "authDomain": "groot-blog.firebaseapp.com",
  "databaseURL": "https://groot-blog.firebaseio.com",
  "projectId": "groot-blog",
  "storageBucket": "groot -blog.appspot.com",
  "messagingSenderId": "803901813580",
  "appId": "1:803901813580:web:18845b43a73584f50755e9",
  "measurementId": "G-TX2N097ECK"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
#db.child("blogposts").push("15")
#db.child("blogposts").push("test")
posts = db.child("blogposts").get()
#print(posts.val())

for post in posts.each():
  print(post.val())
  Document.createElement("p")

web_site = Flask(__name__)
  
#def uploadblog():
#  db.child("blogposts").push("Yeet!")



@web_site.route('/user', methods=['POST'])
def user():
  if request.method == 'POST':

    db.child("blogposts").push(request.form['blog'])  
    return render_template('upload.html')        
#  ...
 # return (request.form['blog'])

  # post = request.args.get("blog")
  # print(post)
  print("h1")
  return True

@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route("/angry")
def angry():
  return render_template('angry.html')

@web_site.route("/calm")
def calm():
  return render_template("calm.html")
  
@web_site.route("/about")
def about():
  return render_template("about.html")

@web_site.route("/upload")
def upload():
  return render_template("upload.html")
web_site.run(host='0.0.0.0', port=8080)




