import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

APP_ID_NUTRITION = os.getenv("APP_ID_NUTRITION")
APP_KEY_NUTRITION = os.getenv("APP_KEY_NUTRITION")
BASE_URL_NUTRITION = os.getenv("BASE_URL_NUTRITION")
HEADERS_NUTRITION = {"x-app-id": APP_ID_NUTRITION, "x-app-key": APP_KEY_NUTRITION, 'Content-Type': 'application/json'}
WEIGHT_KG = float(os.getenv("WEIGHT_KG"))
HEIGHT_CM = float(os.getenv("HEIGHT_CM"))
AGE = int(os.getenv("AGE"))
GENDER = os.getenv("GENDER")
HEADERS_SHEETY = {"Authorization": f"Bearer {APP_KEY_NUTRITION}"}
USERNAME_SHEETY = os.getenv("USERNAME_SHEETY")
PASSWORD_SHEETY = os.getenv("PASSWORD_SHEETY")
BASE_URL_SHEETY = os.getenv("BASE_URL_SHEETY")
PROJECT_NAME_SHEETY = os.getenv("PROJECT_NAME_SHEETY")
SHEET_NAME_SHEETY = os.getenv("SHEET_NAME_SHEETY")

def calculate_calories_burned_from_exercise(exercise_description):
    """
    Calculates the calories burned from exercise
    :param exercise_description: exercise description
    :return: calories burned
    """
    endpoint = BASE_URL_NUTRITION + "/v1/nutrition/natural/exercise" # define the endpoint
    parameters = {
        "query": exercise_description,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
        "gender": GENDER
    } # define the parameters

    response = requests.post(url=endpoint, headers=HEADERS_NUTRITION, json=parameters) # make a post request
    return response.json() # return the response as a JSON object
def add_a_row(date, time, calories):
    """
    Adds a row to the Google Sheet
    :param calories: calories burned
    """
    endpoint = BASE_URL_SHEETY + "/" + USERNAME_SHEETY + "/" + PROJECT_NAME_SHEETY + "/" + SHEET_NAME_SHEETY # define the endpoint
    parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": calories["name"].title(),
            "duration": calories["duration_min"],
            "calories": calories["nf_calories"]
        }
    }

    response = requests.post(url=endpoint, json=parameters, headers=HEADERS_SHEETY) # make a post request
    print(response.text)

exercise_description = input("Tell me which exercises you did: ") # e.g. "walked 6 miles"
calories = calculate_calories_burned_from_exercise(exercise_description) # calculate the calories burned

today_date = datetime.datetime.now().strftime("%d/%m/%Y") # get today's date
now_time = datetime.datetime.now().strftime("%X") # get the current time
add_a_row(today_date, now_time, calories["exercises"][0]) # add a row to the Google Sheet