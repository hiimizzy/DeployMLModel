from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.datasets import load_iris

# Load the Iris dataset to get target names for mapping predictions
iris = load_iris()
target_names = iris.target_names

model = joblib.load('model/iris.pkl') # Load the trained model

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


app = FastAPI()

# define endpoint
@app.post('/predict')
def predict(input: IrisInput):
    try:
        data = np.array([[input.sepal_length, input.sepal_width, 
                          input.petal_length, input.petal_width]])
        
        prediction = model.predict(data)[0]
        class_names = target_names[prediction]

        return {'predicted_class': class_names}

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
    
# uvicorn server:app --reload