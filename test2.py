from turtle import*
lapiz = Turtle()
def cuadrado(p,tamano,color):
    p.color(color)
    p.begin_fill()
    for i in range(4):
        p.forward(tamano)
        p.right(90)
        p.end_fill()

comenzar = input ("Excribe cuadrado").lower()
while comenzar != "detener":
   if comenzar == "cuadrado":
       tamano = int(input("Introduce tamano"))
       color = input("introduce color")
       cuadrado(lapiz,tamano,color)
done() 