import requests
import json

api = "https://alfa-leetcode-api.onrender.com/"
problems = api + "problems"

response = requests.get(problems)

s = response.json()

data = []

for item in s:
    data.append(item)

question_data = s[data[2]]

i = 0
choice = "n"

while choice != "y":
    title = question_data[i].get("title")
    choice = input(f"brev tell me if u wanna do {title}? y/n ")
    if choice == "y":
        print(f"cool lets set up {title}")
        url_title = title.split(" ")
        url_title = "-".join(url_title)
        print(f"https://leetcode.com/problems/{url_title}/description/")
    else:
        i += 1


