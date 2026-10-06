"""Un sistema de pesaje automático genera una lista simple con los pesos (en kg) de varias piezas de metal en una banda transportadora:

pesos_piezas = [12.5, -5.0, 14.2, 0.0, 18.1, 10.5]

Debes:
- Crear un script que recorra esta lista usando un bucle for.
- Utiliza condicionales para clasificar cada pieza:
         -- Si el peso es menor o igual a 0: Imprime "Error de lectura: Flujo negativo descartado."
         -- Si el peso está entre 1 y 13 kg: Imprime "Pieza Ligera aprobada."
         -- Si el peso es mayor a 13 kg: Imprime "Pieza Pesada aprobada."
- Lleva un conteo de cuántas piezas válidas (ligeras + pesadas) pasaron la prueba y muéstralo al final.
"""
pesos_piezas = [12.5, -5.0, 14.2, 0.0, 18.1, 10.5]
cont_ligeras=0
cont_pesadas=0
for i in (pesos_piezas):
    if i <= 0:
        print ("Error de lectura: Flujo negativo descartado.")
    elif i >= 1 and i <= 13:
        print("Pieza Ligera aprobada.")
        cont_ligeras+=1
    else:
        print("Pieza Pesada aprobada.")
        cont_pesadas+=1
total=cont_pesadas + cont_ligeras
print(f"La cantidad de piezas validas fue de {total}, pasaron la prueba final")

