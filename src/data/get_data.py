"""
Script to download the dataset from kaggle.

Author: Tom Fleet
Created: 02/01/2021
"""


from kaggle.api.kaggle_api_extended import KaggleApi

from src.config import RAW_DATA

api = KaggleApi()
api.authenticate()


api.dataset_download_files(
    "saurograndi/airplane-crashes-since-1908", path=RAW_DATA, unzip=True
)
