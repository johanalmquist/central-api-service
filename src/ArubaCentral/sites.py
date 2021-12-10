from pycentral.monitoring import Sites

from .ArubaCentral import central

s = Sites()


def findOrCreate(siteInfo):
    site = s.find_site_id(central, site_name=siteInfo["name"])
    if site is None:
        create(siteInfo)
        return s.find_site_id(central, site_name=siteInfo["name"])

    return site


def create(siteInfo):
    site_address = {
        "address": siteInfo["address"],
        "city": siteInfo["city"],
        "state": siteInfo["state"],
        "zipcode": siteInfo["zipcode"],
        "country": siteInfo["country"],
    }
    site = s.create_site(central, site_name=siteInfo["name"], site_address=site_address)
    return site
