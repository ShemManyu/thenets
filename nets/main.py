import os

from flask import Flask, request, Response, jsonify
from flask_restful import Api
from resources import ChatGroup, Conversation

from authlib.flask.client import OAuth
from loginpass import Google, GitHub, create_flask_blueprint

app = Flask(__name__)

app.config.from_pyfile('config.py')
oauth = OAuth(app)

api = Api(app)

OAUTH_BACKENDS = [
    Google, GitHub
]

@app.route('/login')
def index():
    tpl = '<li><a href="/{}/login">{}</a></li>'
    lis = [tpl.format(b.OAUTH_NAME, b.OAUTH_NAME) for b in OAUTH_BACKENDS]
    return '<ul>{}</ul>'.format(''.join(lis))

def handle_authorize(remote, token, user_info):
    print(user_info)
    return jsonify(user_info)

for backend in OAUTH_BACKENDS:
    bp = create_flask_blueprint(backend, oauth, handle_authorize)
    app.register_blueprint(bp, url_prefix='/{}'.format(backend.OAUTH_NAME))

api.add_resource(ChatGroup, '/groups/<string:group_id>')
api.add_resource(Conversation, '/chat/<string:conversation_id>')

if __name__ == "__main__":
    app.run(debug=True)

#In web browse make sure url is 127.0.0.1:500 
#instead of localhost