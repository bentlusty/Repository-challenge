from repository_challenge import app_service


def main():
    print("Running main service")
    print("Running Processing claims by DB and ES")
    print(app_service.process_claims())
    print("Running Processing claims by csv files")
    print(app_service.process_claims_by_csv())


if __name__ == "__main__":
    main()
