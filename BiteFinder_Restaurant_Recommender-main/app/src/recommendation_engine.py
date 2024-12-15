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
    return filtered.head(5)

if __name__ == '__main__':
    recommendations = recommend_restaurants('New York', 'Italian', 4.0)
    print(recommendations)
