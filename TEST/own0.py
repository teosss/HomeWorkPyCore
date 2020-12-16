from pyowm import OWM

# ---------- FREE API KEY examples ---------------------

owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
Location = input("Enter location = ")
observation = mgr.weather_at_place(Location)
w = observation.weather

dt_s = w.detailed_status         # 'clouds'
speed = w.wind()['speed'] 
deg = w.wind()['deg'] # {'speed': 4.6, 'deg': 330}
humidity = w.humidity                # 87
temp_min = w.temperature('celsius')['temp_max']
temp_max = w.temperature('celsius')['temp_min']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
temp =  w.temperature('celsius')['temp'] 
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

# Will it be clear tomorrow at this time in Milan (Italy) ?
  
print("detailed_status = ", dt_s)
print("temp_min =", temp_min)
print("temp_max =", temp_max)
print("temp =", temp)
print("humidity = ", humidity)
print("speed =", speed)
print("deg = ", deg)
print("rain =", "No rains" if w.rain == {} else w.rain)            
print("heat_index = ", w.heat_index )             # None
print("clouds =", w.clouds)  
