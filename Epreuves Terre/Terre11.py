import sys

if len(sys.argv) != 2:
	print("Erreur")
else:
	time = sys.argv[1]
	res = time.split(":")  #séparer l'heure en deux éléments
if len(res) == 2:
	hour = int(res[0])
	minute = int(res[1])

	if hour > 12:
		hour_12 = hour - 12
		time_period = "PM"
	elif hour == 12:
		hour_12 = 12
		time_period = "PM"
	elif hour == 00:
		hour_12 = 12
		time_period = "AM"
	else:
		hour_12 = hour
		time_period = "AM"
	print(hour_12,':', minute, time_period)
else:
	print("Erreur: Veuillez utiliser le format 00:00")
