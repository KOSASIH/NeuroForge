from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a dictionary of fake user data for development
users = {
    "user1": {
        "username": "user1",
        "name": "User One",
        "password": "password123"
    },
    "user2": {
        "username": "user2",
        "name": "User Two",
        "password": "password456"
    }
}

# Define a dictionary of fake forum data for development
forums = {
    "forum1": {
        "title": "Forum 1",
        "description": "This is forum 1's description.",
        "threads": {
            "thread1": {
                "title": "Thread 1",
                "content": "This is thread 1's content."
            },
            "thread2": {
                "title": "Thread 2",
                "content": "This is thread 2's content."
            }
        }
    },
    "forum2": {
        "title": "Forum 2",
        "description": "This is forum 2's description.",
        "threads": {
            "thread3": {
                "title": "Thread 3",
                "content": "This is thread 3's content."
            }
        }
    }
}

@app.route("/")
def index():
    return redirect(url_for("forums"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username not in users or users[username]["password"] != password:
            return "Invalid username or password"

        # Store user session information here

        return redirect(url_for("forums"))

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        name = request.form["name"]
        password = request.form["password"]

        if username in users:
            return "Username already exists"

        users[username] = {"name": name, "password": password}

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/forums")
def forums():
    # Query forum database here

    return render_template("forums.html", forums=forums)

@app.route("/forum/<string:forum_id>")
def forum(forum_id):
    # Query forum and thread database here

    return render_template("forum.html", forum=forums[forum_id])

@app.route("/thread/<string:forum_id>/<string:thread_id>")
def thread(forum_id, thread_id):
    # Query thread database here

    return render_template("thread.html", thread=forums[forum_id]["threads"][thread_id])

@app.route("/post/<string:forum_id>/<string:thread_id>", methods=["POST"])
def post(forum_id, thread_id):
    # Query thread database here

    return redirect(url_for("thread", forum_id=forum_id, thread_id=thread_id))

@app.route("/logout")
def logout():
    # Clear user session information here

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
