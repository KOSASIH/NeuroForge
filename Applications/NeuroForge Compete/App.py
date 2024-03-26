from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Database configuration
DATABASE_URI = 'sqlite:///competitors.db'

# Connect to database
import sqlite3

def get_db():
    conn = sqlite3.connect(DATABASE_URI)
    conn.row_factory = sqlite3.Row
    return conn

# Add database initialization

@app.before_first_request
def init_db():
    db = get_db()

    # Create competitors table
    db.execute('''
        CREATE TABLE IF NOT EXISTS competitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            score INTEGER DEFAULT 0
        )
    ''')

    # Commit changes
    db.commit()

    # Close connection
    db.close()

# Competitor authentication

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()

        competitor = db.execute('SELECT * FROM competitors WHERE username = ?', (username,)).fetchone()

        if competitor and check_password_hash(competitor['password'], password):
            session['competitor_id'] = competitor['id']
            flash('Login successful!')
            return redirect(url_for('compete'))

        flash('Login failed.')

        db.close()

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        db = get_db()

        db.execute('INSERT INTO competitors (username, email, password) VALUES (?, ?, ?)', (username, email, password))

        db.commit()

        db.close()

        flash('Registration successful.')

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    del session['competitor_id']
    flash('Logout successful.')
    return redirect(url_for('login'))

@app.route('/compete')
def compete():
    if 'competitor_id' not in session:
        return redirect(url_for('login'))

    db = get_db()

    # Get competitor score
    score = db.execute('SELECT score FROM competitors WHERE id = ?', (session['competitor_id'],)).fetchone()[0]

    competitors = db.execute('SELECT * FROM competitors ORDER BY score DESC').fetchall()

    db.close()

    return render_template('compete.html', score=score, competitors=competitors)

@app.route('/submit', methods=['POST'])
def submit():
    if 'competitor_id' not in session:
        return redirect(url_for('login'))

    score = request.form['score']

    db = get_db()

    db.execute('UPDATE competitors SET score = ? WHERE id = ?', (score, session['competitor_id']))

    db.commit()

    db.close()

    flash('Score submitted.')

    return redirect(url_for('compete'))

# Add routes for displaying leaderboard and submitting scores

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'development_key'
    app.run()
