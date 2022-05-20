# def rango(numero: foat):
#     mensaje = ""
#     error_dato = True

#     if numero >= 3.5 and numero < 7.8:
#         error_dato = Falso
#         mensaje +=


#7
menu = """"
| Carácter | Mensaje a imprimir |
|----------|--------------------|
|   'a'    | Android            |
|   'i'    | IOS                |
|   otro   | Opcion inválida    |

elige una opcion: """

opcion = input(menu)

def secion_so (opcion):

    if opcion == 'a' or opcion == 'A':
          return ''


#10
def factura_acueducto(estrato: int, consumo: float, tarifas: dict):
    # Validación
    if estrato < 1 or estrato > 6:
        return "El estrato debe estar entre 1 y 6"
    if consumo < 0:
        return "El consumo debe ser 0 o superior"

    # Proceso
    valor_factura = tarifas[estrato]["cargo_fijo"]
    valor_factura += consumo * tarifas[estrato]["metro_cubico"]
    valor_factura += tarifas[estrato]["basuras"]

    # Salida
    return valor_factura
tarifas = {
    1: { "cargo_fijo": 2500, "metro_cubico": 2200, "basuras": 5500 },
    2: { "cargo_fijo": 2800, "metro_cubico": 2350, "basuras": 6200 },
    3: { "cargo_fijo": 3000, "metro_cubico": 2600, "basuras": 7400 },
    4: { "cargo_fijo": 3300, "metro_cubico": 3400, "basuras": 8600 },
    5: { "cargo_fijo": 3700, "metro_cubico": 3900, "basuras": 9700 },
    6: { "cargo_fijo": 4400, "metro_cubico": 4800, "basuras": 11000 }
}
print(factura_acueducto(2, 23.0, tarifas))

#diccionarios

def desperdicio_de_gaseosa (amigo1, amigo2, amigo3, capacidad_boton):
    pass #instruccion de pase a la sgte linea

amigo1 = {
        "nombre": "harold stiven",
        "capacidad_vaso":10.0,
        "capacidad_actual":5.5
}
amigo2 ={
        "nombre": "camilo hernandez",
        "capacidad_vaso":15.5,
        "capacidad_actual":10.5
}
amigo3 ={
        "nombre": "maria adelaida",
        "capacidad_vaso":5.5,
        "capacidad_actual":2.5
}
print(desperdicio_de_gaseosa(amigo1, amigo2, amigo3, 5.0))
