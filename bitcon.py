import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = "YourApiKeyHere"

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching data from API")
    except (KeyError, ValueError):
        sys.exit("Error parsing API response")

    total_cost = bitcoins * price
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
