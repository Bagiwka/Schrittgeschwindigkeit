#Schrittgeschwindigkeit

    #Input/Deklaration
            #anzahl = 0, damit 'while' funktioniert
anzahl = ''
schrittlaenge = ''
            #ist schrittlaenge eine Zahl?
while(schrittlaenge==''):
            #wenn nicht, dann stelle schrittlaenge auf 0
    schrittlaenge = input("Geben sie die Schrittelaenge in cm ein: ")
    if(schrittlaenge != ''):
        schrittlaenge = int(schrittlaenge)
        break
            #sonst print und wiederhole
    print("Die Schrittlänge darf nicht leer gelassen werden.")
            #solange 'anzahl' kleiner als 0 ist, wiederhole:
while  anzahl =='' or anzahl <= 0:
    anzahl = input("Geben sie die Anzahl der Schritte pro Minute ein: ")
            #wenn 'anzahl' ein leeres string ist (enter gedrückt, ohne etwas zu schreiben)
    if anzahl != '':
        anzahl = int(anzahl)
            #wenn 'anzahl' größer als 0 ist, dann wiederhole nicht mehr
        if(anzahl > 0):

            break
        print("Die Anzahl der Schritte pro Minute müssen größer als 0 sein.")
    else:
        print("Die Anzahl der Schritte pro Minute muss eine Zahl sein.")
            #sonst print und wiederhole
geschwindigkeit = int(schrittlaenge) * int(anzahl)

    #Umrechnung

geschwindigkeit = geschwindigkeit / 6000 * 3.6

    #Ausgabe

print(f"Eine Geschwindigkeit von {geschwindigkeit}km/h wurde erreicht.")

