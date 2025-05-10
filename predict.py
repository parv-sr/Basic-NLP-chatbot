import joblib
import main as m

model = joblib.load('ML_NLP_Model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

def predictIntent():
    input_vector = vectorizer.transform([m.user_input])

    predicted_label = model.predict(input_vector)

    intent = label_encoder.inverse_transform(predicted_label)

    return intent[0]


