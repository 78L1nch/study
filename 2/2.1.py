total_seconds = int(input("Введите секунды: "))

hours = total_seconds // 3600
ostatok = total_seconds % 3600
minutes = ostatok // 60
seconds = ostatok % 60

if hours < 10:
    hours_str = "0" + str(hours)
else:
    hours_str = str(hours)

if minutes < 10:
    minutes_str = "0" + str(minutes)
else:
    minutes_str = str(minutes)

if seconds < 10:
    seconds_str = "0" + str(seconds)
else:
    seconds_str = str(seconds)

print(hours_str + " ч " + minutes_str + " мин " + seconds_str + " с")