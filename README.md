# MyTheresa Scrapy Project

This project is designed to scrape product data from the MyTheresa website using the Scrapy framework. It includes spiders, settings, pipelines, and custom scripts for handling CSV and JSON output. Below is a detailed description of each file and directory within the project.

## Table of Contents
- [Project Structure](#project-structure)
- [File Descriptions](#file-descriptions)
- [How to Use](#how-to-use)

---

## Project Structure

```
├── mytheresa_project/
│   ├── __pycache__/
│   ├── spiders/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── mytheresa_spiderjson.py
│   │   └── mytheresa_spiderscv.py
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
├── duplicatecsv.py
├── duplicatejson.py
├── output.json
├── products.csv
└── scrapy.cfg
```
### File Descriptions

### Root Directory
- **scrapy.cfg**: Scrapy's configuration file for the project. This file defines settings such as the project name and the location of spider modules.
- **products.csv**: Contains the scraped product data in CSV format.
- **output.json**: Contains the scraped product data in JSON format.
- **duplicatecsv.py**: Custom script to check for duplicates in the CSV file, count the total number of data entries, and identify null values.
- **duplicatejson.py**: Custom script to check for duplicates in the JSON output, count the total number of data entries, and identify null values.
- **__pycache__/**: Directory where Python stores the compiled bytecode of modules. This is automatically generated and can be ignored.
  
  
### spiders Directory
- **mytheresa_spiderjson.py**: The spider responsible for scraping product data and outputting it in JSON format.
- **mytheresa_spiderscv.py**: The spider responsible for scraping product data and outputting it in CSV format.
- **__init__.py**: Required for Python to treat this directory as a package.

### Items, Middlewares, Pipelines, and Settings
- **items.py**: Defines the structure for the data being scraped, including fields like product name, price, and more.
- **middlewares.py**: Contains custom middlewares for processing requests and responses.
- **pipelines.py**: Manages the flow of scraped data, including storage in JSON or CSV formats.
- **settings.py**: Configuration file where Scrapy settings specific to this project are defined, such as user agents, concurrent requests, etc.


- ## How to Use

1. **Spider Execution**: 
   - Use the following command to scrape data into a JSON format:
     ```bash
     scrapy crawl mytheresa_spiderjson -o output.json
     ```
   - Use the following command to scrape data into a CSV format:
     ```bash
     scrapy crawl mytheresa_spiderscv
     ```

2. **CSV and JSON Output Handling**: 
   - Use the following command to check for duplicates and analyze the CSV file:
     ```bash
     python3 duplicatecsv.py
     ```
   - Use the following command to check for duplicates and analyze the JSON output:
     ```bash
     python3 duplicatejson.py
     ```
3. **Output Example**: 

   When you run the `duplicatecsv.py` or `duplicatejson.py` scripts, you may see output like the following:
    
    ```
    No duplicates found.
    Products with 'breadcrumbs': 1338
    Products with 'image_url': 1338
    Products with 'brand': 1338
    Products with 'product_name': 1338
    Products with 'listing_price': 1338
    Products with 'offer_price': 0
    Products with 'discount': 0
    Products with 'product_id': 1338
    Products with 'sizes': 1338
    Products with 'other_images': 1338
    Products with 'description': 536
    Total products: 1338
    ```
    
    This output indicates the number of products with specific attributes, along with the total product count, helping users assess the quality and completeness of the scraped data.

