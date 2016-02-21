from flask import Flask,url_for,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return('in index')

@app.route('/login')
def login():
    return('in login')

@app.route('/users/<string:username>')
def profile(username):
    return render_template ('hello.html',name=username)

with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('login',next='/'))
    print (url_for('profile',username = 'Rakesh Hegishte'))
    print (url_for('static',filename='style.css'))
    
if __name__ == '__main__':
    app.run()





    
