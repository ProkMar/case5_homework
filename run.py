from flask import Flask, jsonify, request
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os.path


app = Flask(__name__)


def train_model():
    iris_df = datasets.load_iris()
    data = iris_df.data
    target = iris_df.target
    target_names = iris_df.target_names
    train_data, test_data, train_target, test_target = \
        train_test_split(data, target, test_size=0.3)
    dt = DecisionTreeClassifier().fit(train_data, train_target)
    acc = accuracy_score(test_target, dt.predict(test_data))
    return dt, acc, target_names


def pkl_filename():
    return './data/processed/data_{}.pkl'


def save_data(model, names):
    # Dump the trained decision tree classifier with Pickle
    filename_pattern = pkl_filename()

    # Open the file to save as pkl file
    filename = filename_pattern.format('model')
    with open(filename, 'wb') as file_pkl:
        pickle.dump(model, file_pkl)

    filename = filename_pattern.format('names')
    with open(filename, 'wb') as file_pkl:
        pickle.dump(names, file_pkl)


def load_data():

    model = None
    names = None

    # Loading the saved data
    filename_pattern = pkl_filename()

    filename = filename_pattern.format('model')
    if os.path.exists(filename):
        with open(filename, 'rb') as file_pkl:
            model = pickle.load(file_pkl)

    filename = filename_pattern.format('names')
    if os.path.exists(filename):
        names_pkl = open(filename, 'rb')
        names = pickle.load(names_pkl)

    return model, names


@app.route('/train', methods=['GET'])
def train():
    model, _, names = train_model()
    save_data(model, names)

    answer = jsonify({'class': None,
                      'error': False,
                      'message': "The training of the model is completed"})
    return answer


@app.route('/predict', methods=['POST'])
def predict():

    model, names = load_data()

    if model is None:
        answer = jsonify({'class': None,
                          'error': True,
                          'message': 'Please, train model.'})
    else:
        posted_data = request.get_json()
        sepal_length = posted_data['sepal_length']
        sepal_width = posted_data['sepal_width']
        petal_length = posted_data['petal_length']
        petal_width = posted_data['petal_width']
        prediction = model.predict(
            [[sepal_length, sepal_width, petal_length, petal_width]]
            )[0]

        answer = jsonify({'class': names[prediction],
                          'error': False,
                          'message': "It's OK"})

    return answer


@app.route('/')
def say_iam_here():

    return '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
    <meta charset="UTF-8">
    <title>Hi! I am working!</title>
        <body>

            <ul>
                <li>To train the model, use GET request using the template: 
                http://host_name_or_ip/train</li>

                <li>To get data, use a POST request using the template: 
                http://host_name_or_ip/predict</li>
                <li> or use file request_sample.py</li>
            </ul>

        </body>
    </html>
    '''


model, names = load_data()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
