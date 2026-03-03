import argparse
import os

import requests
from dotenv import load_dotenv

BASE_URL = "https://v6.exchangerate-api.com/v6"


# Gemmer en API-nøgle i .env, hvis brugeren sender --key ved kørsel.
def save_key_if_provided(key: str | None) -> str | None:
    if not key:
        return None

    with open(".env", "w", encoding="utf-8") as env_file:
        env_file.write(f"API_KEY={key}\n")

    return key


# Finder API-nøglen: først fra CLI-argument, ellers fra .env-filen.
def get_api_key(cli_key: str | None) -> str | None:
    saved_key = save_key_if_provided(cli_key)
    if saved_key:
        return saved_key

    load_dotenv()
    return os.getenv("API_KEY")


# Kalder ExchangeRate API'et og returnerer det omregnede beløb.
def convert_currency(
    api_key: str, from_currency: str, to_currency: str, amount: float
) -> float:
    url = f"{BASE_URL}/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url, timeout=10)
    data = response.json()

    if data.get("result") != "success":
        raise ValueError(f"API error: {data.get('error-type', 'unknown')}")

    return data["conversion_result"]


# Starter CLI-programmet, defunerer arguments, henter key og viser resultatet.
def main():
    parser = argparse.ArgumentParser(description="Currency Converter CLI")
    parser.add_argument("--key", help="Your API key")
    parser.add_argument(
        "--from_currency", required=True, help="Currency to convert from"
    )
    parser.add_argument("--to_currency", required=True, help="Currency to convert to")
    parser.add_argument("--amount", type=float, required=True, help="Amount to convert")

    args = parser.parse_args()

    api_key = get_api_key(args.key)
    if not api_key:
        print("I could not find API key. Run once with --key YOUR_API_KEY")
        return

    result = convert_currency(
        api_key,
        args.from_currency.upper(),
        args.to_currency.upper(),
        args.amount,
    )

    print(
        f"{args.amount:.2f} {args.from_currency.upper()} = {result:.2f} {args.to_currency.upper()}"
    )


if __name__ == "__main__":
    main()
