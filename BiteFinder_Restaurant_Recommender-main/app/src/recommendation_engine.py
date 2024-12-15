import os
import pandas as pd
file_path = os.path.join('BiteFinder_Restaurant_Recommender-main', 'app', 'src', 'cleaned_restaurant_data.csv')

def recommend_restaurants(location, cuisine, rating):
    data = pd.read_csv(file_path)
    filtered = data[
        (data['location'].str.contains(location, case=False)) &
        (data['cuisine_type'].str.contains(cuisine, case=False)) &
        (data['rating'] >= rating)
    ]

    # specify the columns to return
    columns_to_return = ['Restaurant Name', 'Address','cuisine_type', 'rating', 'Rating text']  # List of desired columns

# If specific columns are requested, return only those
    if columns_to_return:
        filtered = filtered[columns_to_return]

# Set a specific column as the index
    filtered = filtered.set_index('Restaurant Name')

    return filtered.head(10)

if __name__ == '__main__':
    recommendations = recommend_restaurants('New York', 'Italian', 4.0)
    print(recommendations)
