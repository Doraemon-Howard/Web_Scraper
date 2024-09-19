import requests
from bs4 import BeautifulSoup
import csv

# URL of the Craigslist apartment listings page
url = 'https://newyork.craigslist.org/search/apa#search=1~list~0~0'

# Send a request to the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
 

# Create a list to store the apartment data
apartments = []

# Find all the listings in the results section
for listing in soup.find_all('li', class_='cl-static-search-result'):
    
 
    # Extract the title of the listing
    title = listing.find('div', class_='title').text.strip()
    # Extract the price
    price = listing.find('div', class_='price').text.strip()
    
    # Extract the neighborhood, if available
    neighborhood = listing.find('div', class_='location')
    if neighborhood:
        neighborhood = neighborhood.text.strip()
    else:
        neighborhood = 'N/A'
    
    # Extract the URL of the listing
    link = listing.find('a')['href'].strip() if listing.find('a') else 'N/A'
    
    # Append the data to the apartments list
    apartments.append([title, price, neighborhood, link])

# Write the apartment data to a CSV file
with open('craigslist_apartments_nyc.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Neighborhood', 'URL'])  # CSV header
    writer.writerows(apartments)

print("Scraping completed. Data has been saved to 'craigslist_apartments_nyc.csv'.")
