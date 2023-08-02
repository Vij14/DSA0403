import pandas as pd
Order_data = "C:/Users/91999/Downloads/Order data.xlsx"
total_orders_per_customer = Order_data.groupby('Customer_id').count()['Order_date']

# 2. Average order quantity for each product
average_order_quantity_per_product = Order_data.groupby('Product_name').mean()['Order_quantity']

# 3. Earliest and latest order dates in the dataset
earliest_order_date = order_data['Order_date'].min()
latest_order_date = order_data['Order_date'].max()

# Print the results
print("Total number of orders made by each customer:")
print(total_orders_per_customer)

print("\nAverage order quantity for each product:")
print(average_order_quantity_per_product)

print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
