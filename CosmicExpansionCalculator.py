import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import os

class CosmicExpansionCalculator:
    def __init__(self, target) -> None:
        self.target = target
    
    def getImageFromTarget(self):
        self.coordinates = self.getCoordinates(self.target)
        self.getGIF(self.coordinates[0], self.coordinates[1])

    def getCoordinates(self, target):
        # Set the URL endpoint
        url = "https://stdatu.stsci.edu/cgi-bin/dss_form"

        # Set the query parameters
        params = {
            "target": target,
            "resolver": "SIMBAD"
        }

        # Send the HTTP GET request
        response = requests.get(url, params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # Find the input elements containing the values for RA and Dec
            ra_input = soup.find("input", {"name": "r"})
            dec_input = soup.find("input", {"name": "d"})

            # Extract the values of RA and Dec
            ra_value = ra_input["value"]
            dec_value = dec_input["value"]

            # Print the values
            print("RA:", ra_value)
            print("Dec:", dec_value)
            return (ra_value, dec_value)
        else:
            print("Failed to retrieve the coordinates.")

    def getGIF(self, ra_value, dec_value):
        # Set the URL endpoint
        base_url = "https://stdatu.stsci.edu/cgi-bin/dss_search"

        formatted_ra_value = ra_value.replace(" ", "+")
        formatted_dec_value = quote(dec_value)

        # Set the query parameters
        params = {
            "v": "poss2ukstu_red",
            "r": formatted_ra_value,
            "d": formatted_dec_value,
            "e": "J2000",
            "h": "30",
            "w": "30",
            "f": "gif",
            "c": "none",
            "fov": "NONE",
            "v3": ""
        }

        url = base_url + "?" + "&".join([f"{key}={value}" if key != "v3" else key for key, value in params.items()])

        # Send the HTTP GET request
        response = requests.get(url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Retrieve the image file from the response
            image_data = response.content
            # Save the image file locally
            os.makedirs("cluster_images", exist_ok=True)
            with open(f"cluster_images/{self.target}_image.gif", "wb") as file:
                file.write(image_data)
            print("Image saved successfully.")
        else:
            print("Failed to retrieve the image.")
