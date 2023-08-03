import pandas as pd

# Assuming you have a DataFrame named 'sales_data' with a column 'Age' containing the ages of customers.
# Replace 'sales_data' with the actual name of your DataFrame and 'Age' with the actual column name.

def calculate_age_frequency_distribution(df):
    age_frequency = df['Age'].value_counts().sort_index()
    return age_frequency

def main():
    # Load the sales data into a Pandas DataFrame
    # Replace 'your_sales_data.csv' with the actual filename or path to your sales data CSV file.
    sales_data = pd.read_csv('your_sales_data.csv')

    # Calculate the frequency distribution of ages
    age_frequency_distribution = calculate_age_frequency_distribution(sales_data)

    # Display the frequency distribution
    print("Frequency Distribution of Ages:")
    print(age_frequency_distribution)

if __name__ == "__main__":
    main()
