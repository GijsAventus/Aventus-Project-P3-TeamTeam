#dit bestand gebruiken voor classes (logica & functies)
from math import pi


#class voor opdracht 1
class calculate:
    #functie voor 1.1
    def btw(num):
        try:
            btw = round(float(num) * 0.21, 2)
            return f"De te betalen btw is {btw}."
        except ValueError:
            return "De input is niet geldig."
            
    #functie voor 1.2
    def reistijd(afstand, snelheid):
        try:
            returnValue = f"De reistijd is {str(float(afstand) / float(snelheid))} seconden."
            return returnValue
        except ValueError:
            return "De input is niet geldig."

    #functie voor 1.3
    def vierkant(lengte, breedte):
        try:
            oppervlakte = float(lengte) * float(breedte)
            omtrek = (float(lengte) + float(breedte)) * 2
            string1 = f"Het vierkant heeft een oppervlakte van {oppervlakte}cm en een omtrek van {omtrek}cm."
            return string1
        except ValueError:
            return "De input is niet geldig."

    #functie voor 1.4
    def cirkel(diameter):
        try:
            oppervlakte = ((float(diameter)/2) ** 2) * pi
            omtrek = float(diameter) * pi
            return f"De cirkel heeft een oppervlakte van {str(round(oppervlakte, 2))}cm en een omtrek van {str(round(omtrek, 2))}cm."
        except ValueError:
            return "De input is niet geldig."

    #functie voor 1.5
    def procent(num1, num2):
        try:
            pct = (float(num1) / float(num2)) * 100
            return f"Het getal 1 is {pct} procent in vergelijking met getal 2."
        except ValueError:
            return "De input is niet geldig."
        

#class voor opdracht 2
class relax:
    def __init__(self) -> None:
        pass

#class voor opdracht 3
class xxx:
    def __init__(self) -> None:
        pass