import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
BASE_URL = os.getenv("BASE_URL")
HEADERS = {"x-app-id": APP_ID, "x-app-key": APP_KEY, 'Content-Type': 'application/json'}
WEIGHT_KG = float(os.getenv("WEIGHT_KG"))
HEIGHT_CM = float(os.getenv("HEIGHT_CM"))
AGE = int(os.getenv("AGE"))
GENDER = os.getenv("GENDER")

def calculate_calories_burned_from_exercise(exercise_description):
    endpoint = BASE_URL + "/v1/nutrition/natural/exercise"
    parameters = {
        "query": exercise_description,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
        "gender": GENDER
    }

    response = requests.post(url=endpoint, headers=HEADERS, json=parameters)
    return response.json()
print(calculate_calories_burned_from_exercise("walked 6 miles"))