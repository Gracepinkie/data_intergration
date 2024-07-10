import csv
import json
import sqlite3
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Function to extract data from a CSV file
def extract_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data


# Function to scrape data from an HTML page
def scrape_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Use BeautifulSoup to extract data from the HTML page
        # and return it in a suitable format
        return soup
    

# Function to parse data from an XML file
def extract_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []
    for child in root:
        # Extract data from XML elements and append to data list
        pass
    return data

# Function to read data from a JSON file
def extract_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to initialize SQLite database and create schema
def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS groceries (name TEXT, price REAL)")
    conn.commit()
    conn.close()

# Function to insert data into SQLite database
def insert_data(db_path, data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for row in data:
        values = (row['Name'], row['Price'])
        cursor.execute("INSERT INTO groceries (name, price) VALUES (?, ?)", values)
    conn.commit()
    conn.close()

# Function to search for specific data in SQLite database
def search_data(db_path, query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM groceries WHERE name = ?", (query,))
    result = cursor.fetchall()
    conn.close()
    return result

# Example usage
csv_data = extract_csv('shoprite_data.csv')
xml_data = extract_xml('shoprite_data.xml')
json_data = extract_json('shoprite_data.json')
html_data = scrape_html('shoprite_data.html')


init_db('shoprite.db')
insert_data('shoprite.db', csv_data)
insert_data('shoprite.db', xml_data)
insert_data('shoprite.db', json_data)

# Example search query
search_result = search_data('shoprite.db', 'Python Programming')
print(search_result)

