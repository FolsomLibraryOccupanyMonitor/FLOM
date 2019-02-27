import requests
# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://127.0.0.1:8000/library_monitor/5/enter")
# response = requests.get("http://127.0.0.1:8000/library_monitor/5/enter")
# response = requests.get("http://127.0.0.1:8000/library_monitor/5/leave")

# Print the status code of the response.
print(response.content)
