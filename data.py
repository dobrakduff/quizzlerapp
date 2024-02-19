import requests
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
question_data = response.json()
question_data=question_data["results"]
# print(question_data)