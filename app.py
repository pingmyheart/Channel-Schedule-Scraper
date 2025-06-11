from flask import Flask

from controller import blueprints

app = Flask(__name__)

for blueprint in blueprints:
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=5000,
            debug=False)
