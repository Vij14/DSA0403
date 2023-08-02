item_prices = [2.5, 1.99, 3.25, 4.5]  # Prices of the items
item_quantities = [3, 2, 1, 4]  # Quantities of each item
discount_rate = 10  # 10% discount rate
tax_rate = 8  # 8% tax rate

subtotal = sum(item_price * item_quantity for item_price, item_quantity in zip(item_prices, item_quantities))
discount_amount = (discount_rate / 100) * subtotal
total_after_discount = subtotal - discount_amount
tax_amount = (tax_rate / 100) * total_after_discount
final_total_cost = total_after_discount + tax_amount

print("Final Total Cost:", final_total_cost)
