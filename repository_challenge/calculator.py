from repository_challenge.domain import Claim, Type


def calculate_claim(claim: Claim) -> float:
    # Imagine a lot of calculation here
    if claim.type == Type.BILLABLE:
        return claim.total

    return 0.0
