#Imports tools needed to Build a Server
from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from src.data_processing import preprocess
import datetime


# Brain of Application
app = FastAPI()

#Load the Model
columns = joblib.load("models/columns.pkl")
model = joblib.load("models/model.pkl")

class ChurnInput(BaseModel):
	tenure:int
	MonthlyCharges:float
	TotalCharges:float

@ app.get("/")
def home():
	return {"message": "Churn Prediction API is running"}

@app.post("/predict")

def predict(data: ChurnInput):

	try:
			#convert input into dataframe
		df = pd.DataFrame([data.dict()])

		df = preprocess(df)

		df = df.reindex(columns = columns, fill_value = 0)
		#Predict
		prediction = model.predict(df)[0]
		
		result = "Churn" if prediction == 1 else "No Churn"
		return {
			"TimeStamp":str(datetime.datetime.now()), 
			"Status": "Success",
			"Prediction":int(prediction),
			"Result":result}
	except Exception as e:
		return {
			"Status":"Error",
			"Message":str(e)
		}