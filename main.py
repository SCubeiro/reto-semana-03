import sys

def main():
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
        cantidad = partes[2]
        precio = partes[3]

        # por ahora solo imprimo para verificar que se lee bien
        print(f"{fecha},{producto},{cantidad},{precio}")

if __name__ == "__main__":
    main()
