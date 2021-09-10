
import math
def main():
    # Escribe tu código abajo de esta línea
    radio=float(input('Introduce el radio: '))
    x1=float(input('Introduce x1: '))
    y1=float(input('Introduce y1: '))
    x2=float(input('Introduce x2: '))
    y2=float(input('Introduce y2: '))
    distancia_entre=math.sqrt((x1-x2)**2+((y1+y2)**2))
    if distancia_entre>radio:
        print('FUERA')
    elif distancia_entre==radio:
        print('SOBRE')    
    else:
        print('DENTRO')    

   

if __name__ == '__main__':
    main()
