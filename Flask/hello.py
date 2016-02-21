from flask import Flask
app = Flask(__name__)

@app.route('/')
def Index():
    return 'Index page'

@app.route('/hello/<username>')
def hello_word(username):
    return 'hello %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

if __name__== '__main__':
    app.run()
