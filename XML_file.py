import requests
from bs4 import BeautifulSoup
import pandas as pd
import xml.etree.ElementTree as ET

current_page = 1
data = []

while True:
    print(f'Currently Scraping page: {current_page}')
    url = f'https://shop.shoprite.com/store/{current_page}'  # Adjust the URL for ShopRite groceries

    # Fetch the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if page exists
    if soup.title.text == '404 Not Found':
        break  # Exit the loop if page not found
    else:
        # Extract groceries information
        groceries = soup.find_all('div', class_='product')  # Adjust class name according to ShopRite HTML structure
        
        for grocery in groceries:
            item = {}

            # Extract grocery details
            item['Name'] = grocery.find('span', class_='product-name').text.strip()
            item['Price'] = float(grocery.find('span', class_='product-price').text.strip().replace('$', ''))  # Adjust price extraction based on ShopRite HTML

            data.append(item)

    current_page += 1

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Create XML structure
root = ET.Element('groceries')
for index, row in df.iterrows():
    grocery = ET.SubElement(root, 'grocery')
    name = ET.SubElement(grocery, 'name')
    name.text = row['Name']
    price = ET.SubElement(grocery, 'price')
    price.text = str(row['Price'])

# Create ElementTree object
tree = ET.ElementTree(root)

# Save XML file
tree.write('shoprite_data.xml', encoding='utf-8', xml_declaration=True)


print(df.head())
