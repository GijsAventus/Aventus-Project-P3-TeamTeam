#dit bestand gebruiken voor classes (logica & functies)
from math import pi


#class voor opdracht 1
class calculate:
    #functie voor 1.1
    def btw(num):
        btw = round(num * 0.21, 2)
        return f"De btw is {btw}."
    
    #functie voor 1.2
    def reistijd(afstand, snelheid):
        return f"De reistijd is {str(afstand / snelheid)}"

    #functie voor 1.3
    def vierkant(lengte, breedte):
        oppervlakte = lengte * breedte
        omtrek = (lengte + breedte) * 2
        string1 = f"Het vierkant heeft een oppervlakte van {oppervlakte} en een omtrek van {omtrek}."
        return string1

    #functie voor 1.4
    def cirkel(diameter):
        oppervlakte = ((diameter/2) ** 2) * pi
        omtrek = diameter * pi
        return f"De cirkel heeft een oppervlakte van {str(oppervlakte)[0:5]} en een omtrek van {str(omtrek)[0:5]}."

    #functie voor 1.5
    def procent(num1, num2):
        pct = (num1 / num2) * 100
        return f"Het getal 1 is {pct} procent groot als getal 2."
        

#class voor opdracht 2
class relax:
    def __init__(self) -> None:
        pass

#class voor opdracht 3
class xxx:
    def __init__(self) -> None:
        pass