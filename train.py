from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import preprocess as pr
import joblib


X_train, X_test, y_train, y_test = train_test_split(pr.X, pr.y, test_size=0.2, random_state=42)


model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

try:
    joblib.dump(model, "ML_NLP_Model.pkl")
    joblib.dump(pr.vectorizer, "vectorizer.pkl")
    joblib.dump(pr.le, "label_encoder.pkl")
except Exception as e:
    print("Error while saving.")


