from typing import Optional

import requests


class Inventory:
    def __init__(self):
        self.headers: dict = {"Content-Type": "Application/json"}

    def findDevice(self, serial: Optional[str] = None, mac: Optional[str] = None):
        params: dict = {}
        if serial is not None:
            params["serial"] = serial

        if mac is not None:
            params["mac_address"] = mac

        url = "http://inventory:8002/devices/device"
        req = requests.get(url=url, params=params, headers=self.headers)
        response = req.json()
        if req.reason == "Not Found":
            return None
        else:
            return response

    def findSite(self, site_id: Optional[int] = None, site_name: Optional[str] = None):
        params: dict = {}
        if site_id is not None:
            url = f"http://inventory:8002/sites/site/{site_id}"
            req = requests.get(url=url, headers=self.headers)
            response = req.json()
            return response
        if site_name is not None:
            return params
