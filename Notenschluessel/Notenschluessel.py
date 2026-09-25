prozent = int(input("Wie viel Prozent hast du erreicht? "))
if prozent >= 90:
    note = "Sehr gut)"
elif prozent >=80:
    note = "2 (Gut)"
if prozent >= 65:
    note = "Befriedigend)"
elif prozent >=50:
    note = "2 (Ausreichend )"
else :
    note = "5/6 (Nicht bestanden )"

print ("Deine Note ist", note)


