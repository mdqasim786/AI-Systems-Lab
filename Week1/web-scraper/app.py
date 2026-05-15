import requests
from bs4 import BeautifulSoup
import json

# Website URL
url = "https://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find quote elements
quotes = soup.find_all("span", class_="text")

# Store cleaned data
data = []

for quote in quotes:
    cleaned_quote = quote.text.strip()

    data.append({
        "quote": cleaned_quote
    })

# Save to JSON
with open("quotes.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data saved successfully!")