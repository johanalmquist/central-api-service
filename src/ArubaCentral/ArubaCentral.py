from config import config
from pycentral.base import ArubaCentralBase

central_info = {
    "username": config.CENTRAL_USERNAME,
    "password": config.CENTRAL_PASSWORD,
    "client_id": config.CENTRAL_CLIENT_ID,
    "client_secret": config.CENTRAL_SECRET,
    "customer_id": config.CENTRAL_CUSTOMER_ID,
    "base_url": config.CENTRAL_BASE_URL,
}

central = ArubaCentralBase(central_info=central_info, token_store=None, ssl_verify=True)
