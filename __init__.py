
from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)


app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)




@app.route('/hello', methods=['GET'])
def hello():
    return "hello worlddd";




if __name__ == '__main__':
    app.run()