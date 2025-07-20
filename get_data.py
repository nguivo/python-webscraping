import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.052238&lon=-118.243344")
soup = BeautifulSoup(page.content, 'html.parser')

# Getting the complete 5 day forecast
seven_day_forecast = soup.find(id="seven-day-forecast")
period_tags = seven_day_forecast.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

# short descriptions
shorts = seven_day_forecast.select(".tombstone-container .short-desc")
short_descs = [sd.get_text() for sd in shorts]

# temperatures
tmp = seven_day_forecast.select(".tombstone-container .temp")
temps = [t.get_text() for t in tmp]

descs = [d['title'] for d in seven_day_forecast.select(".tombstone-container img")]


# forecast_items = seven_day_forecast.find_all(class_="tombstone-container")
# today = forecast_items[0]
#
# period = today.find(class_="period-name").get_text()
# short_desc = today.find(class_="short-desc").get_text()
# temp = today.find(class_="temp").get_text()
# img = today.find("img")
# desc = img['title']
# print(img['src'])


