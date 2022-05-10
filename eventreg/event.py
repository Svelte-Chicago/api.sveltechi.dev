import uuid

import firebase_admin
from firebase_admin import credentials, firestore

class events:

    eventlist: list = []

    def __init__(self):
        pass

    def fetchall(self):
        pass

    def register(self, email: str, plus: int = 0) -> bool:
        pass

    def confirm(self, email: str, confirmation: str) -> bool:
        pass

    def update(self, email: str, confirmation: str, plus: int = 0) -> bool:
        pass

    def deregister(self, email: str, confirmation: str) -> bool:
        pass