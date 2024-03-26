from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_network', methods=['POST'])
def create_network():
    architecture = request.form['architecture']
    activation_function = request.form['activation_function']
    learning_rate = float(request.form['learning_rate'])

    # create neural network with specified architecture, activation function, and learning rate
    # ...

    return jsonify({
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True)
