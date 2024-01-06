import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Создаем приложение на Flask
flask_app = Flask(__name__)
model = pickle.load(open("C:\\Users\\пользователь\\Desktop\\IDE\project_diplom\\model_deployment\\model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    
    # переводим ответы из форм в нужные значения
    bin_features = [1 if x=='да' else 0 for x in request.form.values()]
    int_features = [int(x) for x in bin_features]
    features = [np.array(int_features)]
    
    # используем порог для определения класса
    threshold_opt=0.22
    y_pred_proba = model.predict_proba(features)[:, 1]
    y_pred = (y_pred_proba > threshold_opt).astype('int')
    
    # Выводим класс в текстовом виде
    if y_pred == 0:
        y_pred = 'Не получит финансирование'
    else:
        y_pred = 'Получит финансирование'  
    return render_template("index.html", prediction_text = "Класс НКО -  {}".format(y_pred))

if __name__ == "__main__":
    flask_app.run(debug=True)