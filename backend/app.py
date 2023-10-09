from flask import Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)

def init_db():
    print("Initializing database...")
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='posts'")
        if not cursor.fetchone():
            with app.open_resource('schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()
        else:
            print("Table 'posts' already exists.")


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect('database.db')
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/submit', methods=['POST'])
def submit_post():
    # TODO: Implement submit logic
    pass

@app.route('/posts', methods=['GET'])
def get_posts():
    # TODO: Implement retrieve logic
    pass

@app.route('/')
def index():
    return "Welcome to Raghu's Flask App!"


if __name__ == '__main__':
    print("Starting Flask app...")
    init_db()  # Initialize the database
    app.run(debug=True)
