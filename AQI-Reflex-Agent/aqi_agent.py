import csv

def categorize_aqi(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"


def calculate_sub_index(value):
    return value  # simplified rule


def reflex_agent(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pollutants = {
                "PM2.5": float(row["PM25"]),
                "PM10": float(row["PM10"]),
                "NO2": float(row["NO2"]),
                "SO2": float(row["SO2"]),
                "CO": float(row["CO"]),
                "O3": float(row["O3"])
            }

            sub_indices = {k: calculate_sub_index(v) for k, v in pollutants.items()}
            dominant_pollutant = max(sub_indices, key=sub_indices.get)
            aqi = sub_indices[dominant_pollutant]

            print("Pollutant Values:", pollutants)
            print("Dominant Pollutant:", dominant_pollutant)
            print("AQI Value:", aqi)
            print("AQI Category:", categorize_aqi(aqi))
            print("-" * 40)


if __name__ == "__main__":
    reflex_agent("visakhapatnam_aqi.csv")
