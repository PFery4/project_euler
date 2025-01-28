
import os
from urllib import request
from utils.data_directory import DATA_DIRECTORY


def download_file(filename: str) -> None:
    euler_link = f"https://projecteuler.net/resources/documents/{filename}"
    input_file = os.path.join(DATA_DIRECTORY, filename)
    if not os.path.exists(input_file):
        request.urlretrieve(euler_link, input_file)
    assert os.path.exists(input_file)
