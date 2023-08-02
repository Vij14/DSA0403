import numpy as np

# Assuming the 3x3 NumPy array is named "sales_data"
sales_data = np.array([[100, 200, 150],
                       [50, 120, 180],
                       [80, 90, 100]])

# Step 2: Compute the row-wise sum
total_sales_per_product = np.sum(sales_data, axis=1)

# Step 3: Calculate the overall sum of all sales
overall_sum = np.sum(sales_data)

# Step 4: Calculate the average price
total_products = sales_data.shape[0] * sales_data.shape[1]
average_price = overall_sum / total_products

print(f"The average price of all products sold in the past month is: {average_price}")
