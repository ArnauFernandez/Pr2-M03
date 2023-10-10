"""
Adrián Zamora Hernández, Matteo Vilchez, Arnau Fernández
21/09/2023
ASIXc1C M03 UF1 A1
Exemple: AirVolumeCalculator
"""
# Preguntamos al usuario las medidas de la clase una por una
altura = float(input("Cual es la altura de la clase?"))
longitud = float(input("Cual es la longitud de la clase?"))
anchura = float(input("Cual es la anchura de la clase?"))
# Multiplicamos los tres datos
volumen= (anchura*longitud*altura)
# Redondeamos con dos decimales el volumen de la clase
print ("El volumen de la clase es",round(volumen,2),"m3")
