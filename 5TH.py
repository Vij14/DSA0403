import numpy as np

fuel_efficiency = np.array([25.3, 28.7, 22.1, 24.8, 29.5, 26.0, 30.1, 23.5, 27.2, 21.9])

average_fuel_efficiency = np.mean(fuel_efficiency)

index1 = 0  # Replace with the index of the first car model
index2 = 3  # Replace with the index of the second car model

fuel_efficiency_model1 = fuel_efficiency[index1]
fuel_efficiency_model2 = fuel_efficiency[index2]

percentage_improvement = ((fuel_efficiency_model2 - fuel_efficiency_model1) / fuel_efficiency_model1) * 100

print("Average fuel efficiency:", average_fuel_efficiency)
print(f"Percentage improvement between model {index1 + 1} and model {index2 + 1}: {percentage_improvement:.2f}%")
