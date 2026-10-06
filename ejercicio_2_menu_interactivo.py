"""Estás diseñando el menú para controlar los movimientos de un robot. Primero debes mostrar en pantalla las distintas opciones que se tienen
A. Mover a la derecha
B. Mover a la izquierda
C. Mover hacia el frente
D. Mover hacia atrás
E. Apagar

Debes pedirle constantemente al usuario que ingrese un código de comando (A, B, C, D o E). Utiliza un bucle while.

Con la estructura match/case debes indicar (con print) la la acción que realizó el robot en función al código que escribió el usuario:
- "A": "El robot se desplazó a la derecha"
- "B": "El robot se desplazó a la izquierda"
- "C": "El robot se  desplazó hacia adelante"
- "D": "El robot se desplazó hacia atrás"
- "E": Salir del programa (romper el bucle)
- Cualquier otra entrada: "Comando no reconocido. Intente de nuevo."""
movimientos=(input("Ingrese una de las opciones de movmiento del robot:\nA.mover a la derecha\nB.Mover a la izquierda\nC.Mover hacia el frente\nD.Mover hacia atrás\nE.Apagar\n"))
movimientos=movimientos.upper()
while movimientos != "E":
    match movimientos:
        case "A":
            print("El robot se desplazó a la derecha")
        case "B":
            print("El robot se desplazó a la izquierda")
        case "C":
            print("El robot se desplazó hacia adelante")
        case "D":
            print("El robot se desplazó hacia atrás")
        case "E":
            print("Apagando el robot.")
            break
        case _:
            print("Comando no reconocido. Intente de nuevo.")
    movimientos=(input("Ingrese una de las opciones de movmiento del robot:\nA.mover a la derecha\nB.Mover a la izquierda\nC.Mover hacia el frente\nD.Mover hacia atrás\nE.Apagar\n"))
    movimientos=movimientos.upper()
print("Apagando el robot.")
