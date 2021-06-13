__author__ = 'dima masliukovski'

duration = int(input('Enter duration in seconds > '))
print("Duration = ", duration)

seconds_in_minute = 60
seconds_in_hour = 3600
seconds_in_day = 86400

if duration <= seconds_in_minute:
    print(duration, 'сек')
elif duration <= seconds_in_hour:
    seconds = duration % seconds_in_minute
    minutes = (duration - seconds) // seconds_in_minute
    print (minutes, 'мин', seconds, 'сек')
elif seconds_in_hour < duration <= seconds_in_day:
    seconds = duration % seconds_in_minute
    hours = (duration - seconds) // seconds_in_hour
    minutes = (duration - hours * seconds_in_hour )  // seconds_in_minute
    print (hours, 'час', minutes, 'мин', seconds, 'сек')
else:
    seconds = duration % seconds_in_minute
    days = (duration - seconds) // seconds_in_day
    hours = (duration - days * seconds_in_day) // seconds_in_hour
    minutes = (duration - days * seconds_in_day - hours * seconds_in_hour) // seconds_in_minute
    print (days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')   
