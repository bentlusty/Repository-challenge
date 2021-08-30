from time import sleep
from typing import List


def get_claims() -> List[dict]:
    sleep(1)
    return [
        dict(id=1, site_number=1, type="BILLABLE", total=120),
        dict(id=2, site_number=1, type="NOT_BILLABLE", total=140),
        dict(id=3, site_number=2, type="BILLABLE", total=185),
        dict(id=4, site_number=2, type="NOT_BILLABLE", total=1878),
        dict(id=5, site_number=2, type="BILLABLE", total=1),
    ]
