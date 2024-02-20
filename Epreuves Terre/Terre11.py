import time
import sys

heure = sys.argv[1]

format = time.strptime(heure, '%H:%M')

heure_pm = time.strftime('%I:%M %p', format)

print(heure_pm)