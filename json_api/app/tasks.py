import requests
import pandas as pd

from .celery_app import celery_app


@celery_app.task(name="fetch_users_to_csv")
def fetch_users_to_csv():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    # select required fields
    data = [
        {"id": user["id"], "name": user["name"], "email": user["email"]}
        for user in users
    ]

    # create dataframe and save in CSV
    df = pd.DataFrame(data)
    filename = "users_data.csv"
    df.to_csv(filename, index=False)

    return f"Successfully saved to {filename}."