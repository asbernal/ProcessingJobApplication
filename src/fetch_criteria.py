from dataclasses import fields
from src.application import Application

def fetch_criteria():
     return [field.name.replace('_', ' ') for field in fields(Application)]
