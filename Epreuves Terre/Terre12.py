import sys

if len(sys.argv) > 7:
    print("Erreur")
else:
    time = sys.argv[1]
    

    if len(time) == 7:
        hour = time[0:2]
        minute = time[3:5]
        period = time[5:]


        if hour.isdigit() and minute.isdigit():
            hour12 = int(hour)
            minute12 = int(minute)

            if hour12 <= 12 and minute12 <= 59:
                if hour12 < 12 and period == 'PM':
                    hour24 = hour12 + 12
                else:
                    hour24 = hour12
                if hour12 == 12 and period == 'AM':
                    hour24 = hour12 - 12

                    print(hour24, ':', minute)
            else:
                print('Erreur: veuillez utiliser le format 00:00AM/PM')
        else:
            print("Erreur: veuillez utiliser des chiffres")
    else:
        print('Erreur: veuillez utiliser le format 00:00AM/PM')
