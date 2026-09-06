import requests

base_url = "YOUR_BASE_URL"

with open("wordlist.txt", "r") as file:
    for line in file:
        word = line.strip()

        if not word:
            continue

        url = base_url + "/" + word

        try:
            response = requests.get(url, timeout=5)

            if response.status_code != 404:
                print(url, response.status_code)

        except requests.RequestException:
            print(url, "ERROR")