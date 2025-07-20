from get_data import weather_data
import pandas as pd

weather = pd.DataFrame(weather_data)

# Extracting temperature values from data for analysis
search = "(\d+)"
temp_nums = weather["temp"].str.extract(search, expand=False)

# Analysing the weather data
weather["temp_num"] = temp_nums.astype('int')
print(weather["temp_num"])
print(weather["temp_num"].mean())

# selecting periods of low temperature
is_low = weather["temp"].str.contains("Low")
weather["is_low"] = is_low
weather = weather[weather["is_low"]]


print(weather)

