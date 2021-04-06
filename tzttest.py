import pytz
import datetime

country = "Africa/Lagos"
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print(f'The time in {country} is: ', local_time)
print(f'UTC is {datetime.datetime.utcnow()}')

# for countries in pytz.all_timezones:
#     print(countries)
