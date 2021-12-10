""" import os


class Config(object):
    INVENTORY_BASE_URL = os.getenv("INVENTORY_BASE_URL", "")
    CENTRAL_USERNAME = os.getenv("CENTRAL_USERNAME")
    CENTRAL_PASSWORD = os.getenv("CENTRAL_PASSWORS")
    CENTRAL_CLIENT_ID = os.getenv("CENTRAL_CLIENT_ID")
    CENTRAL_SECRET = os.getenv("CENTRAL_SECRET")
    CENTRAL_CUSTOMER_ID = os.getenv("CENTRAL_CUSTOMER_ID")
    CENTRAL_BASE_URL = os.getenv("CENTRAL_BASE_URL")


config = Config """

import os

from dotenv import dotenv_values

dotenv_values()
dir_path = os.path.dirname(os.path.realpath(__file__))


class Config(object):
    CENTRAL_BASE_URL = dotenv_values(".env")["CENTRAL_BASE_URL"]
    CENTRAL_CLIENT_ID = dotenv_values(".env")["CENTRAL_CLIENT_ID"]
    CENTRAL_SECRET = dotenv_values(".env")["CENTRAL_SECRET"]
    CENTRAL_CUSTOMER_ID = dotenv_values(".env")["CENTRAL_CUSTOMER_ID"]
    CENTRAL_USERNAME = dotenv_values(".env")["CENTRAL_USERNAME"]
    CENTRAL_PASSWORD = dotenv_values(".env")["CENTRAL_PASSWORD"]


config = Config
