import math as m

def ejercicio():
    calculo = 6 / 2 * (1 + 2)
    return (calculo)

def  precio_otra_presentacion(producto_gramos: int, precio_producto: float, peso_gramos: int):
    """"Retorna la conversion del precio de un producto en dierentes presentaciones
    """
    precio_conversion = precio_producto * peso_gramos / producto_gramos

  
