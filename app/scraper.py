import logging
import json
import csv

import requests
from bs4 import BeautifulSoup


logging.basicConfig(filename='log.txt', level=logging.DEBUG)


class PackagePypiParser:

    def __init__(self, search_term):
        self.search_term = search_term
        self.url = f"https://pypi.org/search/?q={search_term}"
        self.packages = []

    def parse(self) -> list[dict]:

        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        package_snippets = soup.find_all("a", class_="package-snippet")

        try:

            for package_snippet in package_snippets:
                name_elem = package_snippet.find("span", class_="package-snippet__name")
                name = name_elem.text.strip() if name_elem else "No name"
                logging.info(f'Package element {name} received')

                version_elem = package_snippet.find("span", class_="package-snippet__version")
                version = version_elem.text.strip() if version_elem else "No version information"

                created_elem = package_snippet.find("span", class_="package-snippet__created")
                created = created_elem.text.strip() if created_elem else "no creation data information"

                package_data = {
                    "name": name,
                    "version": version,
                    "created": created
                }

                self.packages.append(package_data)
                logging.info('Pac received')

            if len(self.packages) > 0:

                return self.packages
            
            else:
                return False              
                    
        except Exception as ex:
            print(f'Error: {ex}')
    
    def save_to_json(self) -> None:
        filename = self.search_term
        with open(f'output/{filename}.json', "w") as f:
            json.dump(self.packages, f)

    def save_to_csv(self):
        filename = self.search_term
        with open(f'output/{filename}.csv', "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "version", "created"])
            for package in self.packages:                
                writer.writerow([package["name"], package["version"], package["created"]])
