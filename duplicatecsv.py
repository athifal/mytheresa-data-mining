import pandas as pd

# Load the CSV file
df = pd.read_csv('products.csv')

# Function to check for duplicates in groups of 9 rows, excluding the first column
def check_group_duplicates(df, group_size=9):
    # Exclude the first column
    df = df.iloc[:, 1:]

    # Create a new DataFrame to hold the grouped rows as strings
    grouped_rows = []

    for i in range(0, len(df), group_size):
        # Get the next group of 9 rows
        group = df.iloc[i:i + group_size]
        # Convert the group to a string representation
        grouped_rows.append(group.to_string(index=False))

    # Check for duplicates among the grouped rows
    seen_groups = {}
    duplicates_count = 0

    for idx, group in enumerate(grouped_rows):
        if group in seen_groups:
            seen_groups[group].append(idx)  # Store the index of the duplicate group
            duplicates_count += 1
        else:
            seen_groups[group] = [idx]

    # Output results
    if duplicates_count > 0:
        print(f"Duplicate groups found: {duplicates_count}")
    else:
        print("No duplicates found.")

# Function to count fields with available examples
def count_fields_with_examples(df, field_names):
    counts = {}
    total_products = len(df)

    for field in field_names:
        example_count = df.loc[df['Field Name'] == field, 'Example'].count()
        counts[field] = example_count

    return int(total_products/9), counts

# Check for duplicate groups of 9 rows, excluding the first column
check_group_duplicates(df)

# Define fields to check
fields_to_check = ['breadcrumbs', 'product_image', 'brand_name', 'product_name', 
                   'product_price','product_id', 'Sizes', 
                   'other_images', 'Description']

# Count fields with available examples
total_products, available_counts = count_fields_with_examples(df, fields_to_check)

# Output the total products and counts for each field
print(f"Total products: {total_products}")
for field in fields_to_check:
    count = available_counts.get(field, 0)
    print(f"Products with '{field}': {count}")
