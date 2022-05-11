import uuid
import json
import os

import firebase_admin
from firebase_admin import credentials, firestore


class EventLoadError(Exception):
    pass

class event:

    _credentials: dict = {}
    _data: dict = {}

    def __init__(self, event_id: str):
        try:
            self._credentials= json.loads(os.getenv("GOOGLE_AUTH"))
        except json.decoder.JSONDecodeError as jde:
            pass

    def details(self) -> dict:
        pass

    def register(self, registration: dict) -> bool:
        pass

    def confirm(self, event_id: str, email: str, confirmation: str) -> bool:
        pass

    def update(self, event_id: str, email: str, confirmation: str, plus: int = 0) -> bool:
        pass

    def deregister(self, event_id: str, email: str, confirmation: str) -> bool:
        pass