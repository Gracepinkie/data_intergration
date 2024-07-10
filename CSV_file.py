import requests
from bs4 import BeautifulSoup
import pandas as pd

current_page = 1

data = []

proceed = True

while(proceed):
    print('Currently Scraping page: '+str(current_page))
    url = f'https://shop.shoprite.com/store/{current_page}' 

    page = requests.get(url)

    soup = BeautifulSoup(page.text,'html.parser')

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

# Convert the data list into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv('shoprite_data.csv', index=False)

print(df.head())




