from flask import Flask, render_template, request, jsonify
from event_models import Event
from sqlalchemy_object import db
from sleep_database_handler import sleep_storer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/clarity'
db.init_app(app)

@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html',events=events)

@app.route('/sleep', methods=["POST"])
def sleep():
    data = request.get_json()
    sleep_storer(data)
    return jsonify({"ok": True})



if __name__ == '__main__':
    app.run(debug=True)