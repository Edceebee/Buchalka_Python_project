import webbrowser
import time

# webbrowser.open('https://www.google.com/')
# help(webbrowser)

time_here = time.localtime()
print(time_here)
print('Year:',  time_here.tm_year)
print('Month:',  time_here.tm_mon)
print('Day:',  time_here.tm_mday)

