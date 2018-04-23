import random
# Python-Grundlagen.py

# Kommentare erfolgen mit hashtag

# Ausgabe von Daten
print("Hallo World")

# Variable definieren (kann ohne Typ erfolgen)
heimat = "Erde"

# Mehrere Variablen werden mit "," getrennt
print(heimat, "an World:, Hello!")

# Eingabe / liest Text(!) von der Konsole ein
wer = input("Und wer bist du? ")

# und gibt den Text wieder aus
if(wer == "ich"):
    print("Hallo Du! ")
else:
    print("Hallo", wer, "!")

lieblingszahl = input("Was ist deine Lieblingszahl? ")
print("Super, ich mag die Zahl", lieblingszahl, "auch!")
print("Aber die groessere Zahl", int(lieblingszahl) +10, "mag ich noch mehr! ")

runden = input("Wieviele Runden sollen wir spielen? ")
runden = int(runden)

sieger = ""
siegerC = ""
gewinn = 0
gewinnC = 0
for runde in range(1, runden +1):
    # Zufallszahl erzeugen
    zufallszahl = random.randint(1,6)
    if(zufallszahl == 1 or zufallszahl == 3 or zufallszahl == 5):
        sieger = wer
        gewinn += 1 
    else:
        sieger = "Computer"
        gewinnC += 1 
    print("Runden", runde, "von", runden, ": Sieger: ", sieger, "   gewuerfelt wurde: ", zufallszahl)
if(gewinn > gewinnC):
    print("Der Gesamtgewinner ist", wer, ".")
else:
    print("Der Gesamtgewinner ist der Computer.")
elif(gewinn == gewinnC):
    print("Es gibt keinen Gewinner! Unentschieden.")
print(wer, "hat", gewinn,"mal gewonnen und der Computer gewann", gewinnC, "mal.")
print("Game over...")