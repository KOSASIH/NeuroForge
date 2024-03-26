from flask import Flask

app = Flask(__name__)

# Import routes
from controllers.deploy import app as deploy_app

app.register_blueprint(deploy_app, url_prefix='/deploy')

if __name__ == '__main__':
    app.run(debug=True)
