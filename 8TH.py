import pandas as pd

# Assuming you have the sales_data DataFrame
# sales_data = pd.DataFrame(...)

# Group the data by product name and sum the quantities sold for each product
product_sales = sales_data.groupby('product_name')['quantity_sold'].sum()

# Sort the products based on the total quantities sold in descending order
top_products = product_sales.sort_values(ascending=False)

# Select the top 5 products
top_5_products = top_products.head(5)

# Print the result
print("Top 5 products with the most sales in the past month:")
print(top_5_products)

