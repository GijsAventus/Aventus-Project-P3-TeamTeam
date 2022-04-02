#dit bestand gebruiken voor classes (logica & functies)
from math import pi


#class voor opdracht 1
class calculate:
    def btw(num):
        return (num * 1.21) - num
    
    def reistijd(afstand, snelheid):
        return f"De reistijd is {str(afstand / snelheid)}"

    def vierkant(lengte, breedte):
        oppervlakte = lengte * breedte
        omtrek = (lengte + breedte) * 2
        string1 = f"Het vierkant heeft een oppervlakte van {oppervlakte} en een omtrek van {omtrek}."
        return string1

    def cirkel(diameter):
        oppervlakte = ((oppervlakte/2) ** 2) * pi
        omtrek = diameter * pi
        return f"Deze cirkel heeft een oppervlakte van {oppervlakte} en een omtrek van {omtrek}."

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

print(calculate.cirkel(5))