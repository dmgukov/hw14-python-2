import requests


def check_addresses(address_list):
    # remove new line characters
    address_list = [x.strip() for x in address_list]

    # list value to collect non-working addresses
    results_list = []

    for address in address_list:
        try:
            response = requests.get(address, timeout=5)
            if response.status_code != 200:
                results_list.append(address)
        except requests.exceptions.Timeout:
            results_list.append(f"{address} timed out after 5 seconds")
        except requests.exceptions.RequestException:
            results_list.append(f"Failed to establish a connection with {address}")
    return results_list


with open("address_list.txt") as f:
    address_list = f.readlines()

results = check_addresses(address_list)
print(results)