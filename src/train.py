from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


from data_processing import load_data, preprocess

#1. Load Data
df = load_data("../data/Churn.csv")

#2. Preprocess Data
df = preprocess(df)



#3. Split Features &  Target
X = df.drop("Churn_Yes", axis = 1)
y = df[["Churn_Yes"]]

joblib.dump(list(X.columns), "../models/columns.pkl")
#4. Train Test Split
X_train,X_test,y_train,y_test = train_test_split(X,y,
                                                 test_size = 0.2, random_state = 42)

# 6. Train Model
model = RandomForestClassifier()
model.fit(X_train,y_train)

# 7. Predict
preds = model.predict(X_test)

# 8. Evalute
print("Accuracy: ",accuracy_score(y_test,preds))

#9. Save Model
joblib.dump(model, "../models/model.pkl")
