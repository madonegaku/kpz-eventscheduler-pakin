# src/models/event.py
from datetime import datetime

class Event:
    def __init__(self, title, start_time, description=""):
        self.title = title
        self.start_time = start_time
        self.description = description
        self.created_at = datetime.now()