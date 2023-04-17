import requests


def check_addresses(address_list):
    # remove new line characters
    address_list = [x.strip() for x in address_list]

    for address in address_list:
        try:
            response = requests.get(address, timeout=5)
            if response.status_code != 200:
                print(f"{address} returned a status code of {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"{address} timed out after 5 seconds")
        except requests.exceptions.RequestException:
            print(f"Failed to establish a connection with {address}")


with open("address_list.txt") as f:
    address_list = f.readlines()

check_addresses(address_list)