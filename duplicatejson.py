import json

# Load your JSON data
with open('output.json', 'r') as f:
    data = json.load(f)

# Function to check for duplicate objects
def check_duplicates(data):
    seen_products = []
    duplicates = []

    for product in data:
        if product in seen_products:
            duplicates.append(product)
        else:
            seen_products.append(product)
    
    return duplicates

# Count total products and check how many have values for each of the 11 fields
def count_key_attributes(data, fields):
    total_products = len(data)
    counts = {field: sum(1 for product in data if product.get(field)) for field in fields}
    counts['total_products'] = total_products
    return counts
fields_to_check = [
    'breadcrumbs', 'image_url', 'brand', 'product_name', 
    'listing_price', 'offer_price', 'discount', 
    'product_id', 'sizes', 'other_images', 'description'
]

# Call the function to find duplicates
duplicates = check_duplicates(data)

# Call the function to count total products and key attributes
attribute_counts = count_key_attributes(data, fields_to_check)

# Output result for duplicates
if duplicates:
    print(f"Found {len(duplicates)} duplicate(s):")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("No duplicates found.")

# Output the count of products and key attributes
for field in fields_to_check:
    print(f"Products with '{field}': {attribute_counts[field]}")
print(f"Total products: {attribute_counts['total_products']}")
