from time import sleep


def get_sites_by_site_number(site_number: int) -> dict:
    sleep(1)
    sites = [dict(id=1, name="JomaShop"), dict(id=2, name="EBAY")]
    return next(x for x in sites if x["id"] == site_number)
