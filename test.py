import requests

API_KEY = "greycat78"
EMAIL = "jbhumph@gmail.com"


url = "https://aqs.epa.gov/data/api/annualData/byState"
params = {
    "email": EMAIL,
    "key": API_KEY,
    "param": "44201",
    "bdate": "20230101",
    "edate": "20231231",
    "state": "53"
}

try:
    response = requests.post(url, json=params, timeout=10)
    response.raise_for_status()
    print("Response:", response.json())
except requests.exceptions.Timeout:
    print("Error: Request timed out")
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API")
except requests.exceptions.RequestException as e:
    print("API Request Failed:", str(e))
print("Status Code:", response.status_code)
print("Response Text:", response.text)