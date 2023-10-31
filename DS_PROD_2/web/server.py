from flask import Flask, request, jsonify
import pickle
import numpy as np

with open('C:\\Users\\пользователь\\Desktop\\IDE\DS_PROD_2\\web\\models\\model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

app = Flask(__name__)


@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg


@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json)
    features = features.reshape(1, 4)
    prediction = model.predict(features)
    return  jsonify({'prediction': prediction[0]})


if __name__ == '__main__':
    app.run('localhost', 5000)