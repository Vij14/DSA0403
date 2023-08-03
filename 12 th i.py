import matplotlib.pyplot as plt

def create_temperature_line_plot(months, temperatures):
    plt.figure(figsize=(10, 6))  # Optional: Set the figure size (width, height) in inches

    plt.plot(months, temperatures, marker='o', linestyle='-', color='b', label='Temperature (°C)')

    plt.title('Monthly Temperature Data')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.legend()

    plt.grid(True)  # Optional: Display grid lines

    plt.xticks(rotation=45)  # Optional: Rotate the x-axis labels if they are too long
    plt.tight_layout()  # Optional: Adjusts the spacing of the plot

    plt.show()

# Example data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperatures = [15, 17, 20, 25, 28, 30, 32, 31, 29, 26, 22, 18]

create_temperature_line_plot(months, temperatures)
