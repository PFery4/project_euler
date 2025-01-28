import os

DATA_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
os.makedirs(DATA_DIRECTORY, exist_ok=True)
