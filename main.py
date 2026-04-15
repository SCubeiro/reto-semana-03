import sys

def main():
    # Diccionario para agrupar por producto
    productos = {}

    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        # Saltar encabezado
        if primera_linea:
            primera_linea = False
            continue

        if not linea:
            continue

        partes = linea.split(',')
        if len(partes) != 4:
            continue

        fecha = partes[0]
        producto = partes[1]
        cantidad = int(partes[2])
        precio = float(partes[3])

        # Si el producto no existe, crearlo
        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }

        # Acumular valores
        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    # Calcular precio promedio por producto
    for prod in productos:
        unidades = productos[prod]["unidades"]
        ingreso = productos[prod]["ingreso"]
        productos[prod]["promedio"] = ingreso / unidades

    # Ordenar por ingreso total descendente
    productos_ordenados = sorted(
        productos.items(),
        key=lambda x: x[1]["ingreso"],
        reverse=True
    )

    # Imprimir salida CSV
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for nombre, datos in productos_ordenados:
        print(f"{nombre},{datos['unidades']},{datos['ingreso']:.2f},{datos['promedio']:.2f}")

if __name__ == "__main__":
    main()
