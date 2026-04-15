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

    # Debug: imprimir lo que tenemos
    for prod, datos in productos.items():
        print(f"{prod}: {datos}")

if __name__ == "__main__":
    main()
