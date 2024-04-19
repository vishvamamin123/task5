import requests
from bs4 import BeautifulSoup
import csv


def scrape_flipkart_laptops(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all laptop containers
    laptops = soup.find_all('div', class_='_1AtVbE')

    # Create a list to store laptop information
    laptop_data = []

    for laptop in laptops:
        # Extract laptop name
        name_element = laptop.find('div', class_='_4rR01T')
        if name_element:
            name = name_element.text.strip()
        else:
            name = 'N/A'

        # Extract laptop price
        price_element = laptop.find('div', class_='_30jeq3 _1_WHN1')
        if price_element:
            price = price_element.text.strip()
        else:
            price = 'N/A'

        # Extract laptop rating
        rating_element = laptop.find('div', class_='_3LWZlK')
        if rating_element:
            rating = rating_element.text.strip()
        else:
            rating = 'N/A'

        # Append laptop information to the list
        laptop_data.append([name, price, rating])

    return laptop_data


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Price', 'Rating'])
        writer.writerows(data)


if __name__ == "__main__":
    # URL of the Flipkart page to scrape
    flipkart_url = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree'

    # Scrape laptop information from Flipkart
    laptop_data = scrape_flipkart_laptops(flipkart_url)

    # Save laptop information to a CSV file
    save_to_csv(laptop_data, 'flipkart_laptops.csv')