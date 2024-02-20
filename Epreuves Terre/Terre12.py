import sys
import time 

heure = sys.argv[1]

format_12h = time.strptime(heure, '%I:%M%p')

heure_24h = time.strftime('%H:%M', format_12h)

print(heure_24h)