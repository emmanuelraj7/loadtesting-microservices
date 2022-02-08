
import time
import json
from locust import HttpUser, task, between


test_data = json.dumps({
    "temp_c": 8.75,
    "humidity": 0.83,
    "wind_speed_kmph": 70,
    "wind_bearing_degree": 259,
    "visibility_km": 15.82,
    "pressure_millibars": 1016.51,
    "current_weather_condition": 1
})
headers = {'Content-Type': 'application/json'}


class MLServiceUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_weather_predictions(self):
        self.client.post("", data=test_data, headers=headers)
