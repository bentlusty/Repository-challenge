import csv
from pathlib import Path
from typing import TypedDict

from repository_challenge import orm, calculator, es
from repository_challenge.domain import Claim, Type


class Result(TypedDict):
    number_of_billable_claim: int
    total: float


def calculate_claims() -> Result:
    number_of_billable_claim = 0
    total = 0
    claims = es.get_claims()

    for claim in claims:
        site = orm.get_sites_by_site_number(claim["site_number"])
        claim_domain = Claim(
            id=claim["id"],
            merchant_name=site["name"],
            type=Type(claim["type"]),
            total=float(claim["total"]),
        )
        total += calculator.calculate_claim(claim_domain)
        if total != 0:
            number_of_billable_claim += 1
    return Result(number_of_billable_claim=number_of_billable_claim, total=total)


def _convert_csv_type_to_domain_type(type: str) -> Type:
    if type == "Billable":
        return Type.BILLABLE
    if type == "Not_Billable":
        return Type.NOT_BILLABLE


def calculate_claims_by_csv() -> Result:
    number_of_billable_claim = 0
    total = 0
    csv_path = Path("./claims-2021-01-02.csv")
    with csv_path.open("r") as f:
        reader = csv.DictReader(f)
        for claim in reader:
            claim_domain = Claim(
                id=int(claim["id"]),
                merchant_name=claim["name"],
                type=_convert_csv_type_to_domain_type(claim["type"]),
                total=float(claim["total"]),
            )
            total += calculator.calculate_claim(claim_domain)
            if total != 0:
                number_of_billable_claim += 1

    return Result(number_of_billable_claim=number_of_billable_claim, total=total)
