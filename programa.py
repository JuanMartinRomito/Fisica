#Parte 2 ejercicio 1 Emilia Ortega, Lucio Manitta y Juanmartin Romito
repeticion=int(input("Cuantas veces queres que se repita el codigo: "))
lista=[]

for i in range(0,repeticion):
    def variables():
        vel= float(input("ingrese la velocidad (m/s): "))
        cabal=float(input("ingrese la distancia del caballo hasta el auto(m): "))
        fren= float(input("ingrese a que velocidad el auto desacelera(m/s): "))
        while fren>0:
            fren= float(input("NO se puede la desaceleracion numero positivo ponelo en negativo: "))
            if fren<0:
                break
        return calculos(vel, cabal, fren)
    def calculos(vel, cabal, fren):
        calc= 0-vel
        tie= calc/fren
        dist= 0+vel*tie+0.5*fren*(tie*tie)
        if dist>cabal:
            print("Te tragaste a un caballo de frente pobre de el :(")
            c = vel + (1/2)*(0-vel)
            c2 = cabal/c
            acel = (0-vel)/c2
            print("nececitabas frenar a ", acel, "m/s2 para no chocarte")
            print("lo chocaste en ",tie, "segundos")
            lista.append(acel)
            lista.append(tie)
        elif dist<=cabal:
            dist2=cabal-dist
            print("te quedaste a",dist2, "metros de chocar al caballo")
            print("Frenaste en ",tie, "segundos")
            lista.append(dist2)
            lista.append(tie)
    variables()
print("los resultados de los calculos fueron ",lista)

## Comentario para modificar el archivo