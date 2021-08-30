from repository_challenge import calculate_claims


def main():
    print("Running main service")
    print("Running Processing claims by DB and ES")
    print(calculate_claims.calculate_claims_by_csv())
    print("Running Processing claims by csv files")
    print(calculate_claims.calculate_claims())


if __name__ == "__main__":
    main()
