import pandas as pd
import glob
import os

def load_data(folder_path):
    # Load all CSV files from the specified folder
    file_paths = glob.glob(os.path.join(folder_path, '*.csv'))
    data_frames = []
    for file in file_paths:
        df = pd.read_csv(file)
        if not df.empty:
            data_frames.append(df)
    if data_frames:
        return pd.concat(data_frames, ignore_index=True)
    else:
        raise ValueError("No valid CSV files to process.")

def calculate_monthly_and_seasonal_averages(df):
    # Monthly columns specified in the dataset
    monthly_columns = ['January', 'February', 'March', 'April', 'May', 'June', 
                       'July', 'August', 'September', 'October', 'November', 'December']

    # Calculate the average for each month
    monthly_avg = df[monthly_columns].mean()
    
    # Mapping months to seasons
    seasons = {
        'Winter': ['June', 'July', 'August'],
        'Spring': ['September', 'October', 'November'],
        'Summer': ['December', 'January', 'February'],
        'Autumn': ['March', 'April', 'May']
    }

    # Calculate seasonal averages
    seasonal_avg = pd.Series({season: df[months].mean().mean() for season, months in seasons.items()})
    
    # Save the results
    monthly_avg.to_csv('monthly_averages.csv', header=['Average Temperature'])
    seasonal_avg.to_csv('average_temp.txt', header=['Average Temperature'])

def find_extreme_temperatures(df):
    # Combine all monthly data into a single DataFrame for range calculations
    monthly_columns = ['January', 'February', 'March', 'April', 'May', 'June', 
                       'July', 'August', 'September', 'October', 'November', 'December']
    df['Max Temperature'] = df[monthly_columns].max(axis=1)
    df['Min Temperature'] = df[monthly_columns].min(axis=1)
    df['Temperature Range'] = df['Max Temperature'] - df['Min Temperature']
    
    # Find the station with the largest temperature range
    max_range_station = df[df['Temperature Range'] == df['Temperature Range'].max()]
    max_range_station[['STATION_NAME', 'Temperature Range']].to_csv('largest_temp_range_station.txt', index=False)

    # Find the warmest and coolest stations based on average annual temperature
    df['Average Annual Temperature'] = df[monthly_columns].mean(axis=1)
    warmest_station = df[df['Average Annual Temperature'] == df['Average Annual Temperature'].max()]
    coolest_station = df[df['Average Annual Temperature'] == df['Average Annual Temperature'].min()]
    extremes = pd.DataFrame({
        'Warmest Station': warmest_station['STATION_NAME'].values,
        'Coolest Station': coolest_station['STATION_NAME'].values
    })
    extremes.to_csv('warmest_and_coolest_station.txt', index=False)

def main():
    folder_path = r"C:/Users/User/Downloads/HIT137 Assignment 2 SS 2024/temperature_data"
    df = load_data(folder_path)
    
    calculate_monthly_and_seasonal_averages(df)
    find_extreme_temperatures(df)
    print("Analysis completed. Results are saved to files.")

if __name__ == "__main__":
    main()
