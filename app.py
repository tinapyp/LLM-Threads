import os
from threadspy import ThreadsAPI

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

api = ThreadsAPI(username=USERNAME, password=PASSWORD)
api.publish(caption="Test Post from API!")
