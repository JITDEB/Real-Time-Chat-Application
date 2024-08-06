from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
socketio = SocketIO(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from routes.auth_routes import auth as auth_blueprint
from routes.chat_routes import chat as chat_blueprint
app.register_blueprint(auth_blueprint)
app.register_blueprint(chat_blueprint)

if __name__ == '__main__':
    socketio.run(app, debug=True)
