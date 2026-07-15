peliculas = {
    "P101": ["Luz de Otoño", "drama", 110, "B", "Español", False],
    "P102": ["Noche Neón", "acción", 125, "C", "Ingles", True],
    "P103": ["Planeta Agua", "documental", 90, "A", "Español", False],
    "P104": ["Risa Total", "comedia", 105, "A", "Español", True],
    "P105": ["Código Zero", "thriller", 118, "C", "Ingles", True],
    "P106": ["Viaje Lunar", "ciencia ficción", 132, "B", "Ingles", False]
}

cartelera = {
    "P101": [5990, 40],
    "P102": [7990, 0],
    "P103": [4990, 25],
    "P104": [6990, 12],
    "P105": [8990, 8],
    "P106": [7490, 3]
}


def validar_texto(texto):
    return texto.strip()!=" "
def validar_duracion(duracion):
    return duracion>=0
def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ["A","B","c"]
def validar_es3d(es3d):
    return es3d.lower() in ["s","n"]
def validar_precio(precio):
    return precio>=0
def validar_cupos(cupos):
    return cupos>=0

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida")
        except:
            print("Debe ingresar un número entero")


def buscar_codigo(codigo, cartelera):
    codigo = codigo.upper()
    return codigo in cartelera


def cupos_genero(genero, peliculas, cartelera):
    total = 0
    for codigo in peliculas:
        if peliculas[codigo][1].lower() == genero.lower():
            total += cartelera[codigo][1]
    print("El total de cupos disponibles es:", total)


def busqueda_precio(p_min, p_max, peliculas, cartelera):
    lista = []
    for codigo in cartelera:
        if cartelera[codigo][0] >= p_min and cartelera[codigo][0] <= p_max and cartelera[codigo][1] > 0:
            titulo = peliculas[codigo][0]
            lista.append(titulo + "--" + codigo)

    lista.sort()

    if len(lista) == 0:
        print("No hay películas en ese rango de precios.")
    else:
        print("Las películas encontradas son:", lista)


def actualizar_precio(codigo, nuevo_precio, cartelera):
    codigo = codigo.upper()
    if codigo in cartelera:
        cartelera[codigo][0] = nuevo_precio
        return True
    return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    codigo = codigo.upper()
    if codigo in cartelera:
        return False

    peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d]
    cartelera[codigo] = [precio, cupos]
    return True


def eliminar_pelicula(codigo, peliculas, cartelera):
    codigo = codigo.upper()
    if buscar_codigo(codigo, cartelera):
        del peliculas[codigo]
        del cartelera[codigo]
        return True
    return False


def main():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")

        opcion = leer_opcion()

        if opcion == 1:
            genero = input("Ingrese género a consultar: ")
            cupos_genero(genero,peliculas,cartelera)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= p_min:
                        busqueda_precio(p_min,p_max,peliculas,cartelera)
                        break
                    print("Debe ingresar valores enteros")
                except:
                    print("Debe ingresar valores enteros")

        elif opcion == 3:
            seguir = "s"
            while seguir.lower() == "s":
                codigo = input("Ingrese código de película: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        if actualizar_precio(codigo,nuevo_precio,cartelera):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("Precio inválido")
                except:
                    print("Precio inválido")

                seguir = input("¿Desea actualizar otro precio (s/n)?: ")

        elif opcion == 4:
            codigo = input("Ingrese código de película: ")
            titulo = input("Ingrese título: ")
            genero = input("Ingrese género: ")

            try:
                duracion = int(input("Ingrese duración (minutos): "))
            except:
                duracion = ""

            clasificacion = input("Ingrese clasificación: ").upper()
            idioma = input("Ingrese idioma: ")
            es_3d = input("¿Es 3D? (s/n): ")

            try:
                precio = int(input("Ingrese precio: "))
            except:
                precio = ""

            try:
                cupos = int(input("Ingrese cupos: "))
            except:
                cupos = ""

            if not validar_texto(codigo):
                print("Código inválido")
            elif not validar_texto(titulo):
                print("Título inválido")
            elif not validar_texto(genero):
                print("Género inválido")
            elif not validar_duracion(duracion):
                print("Duración inválida")
            elif not validar_clasificacion(clasificacion):
                print("Clasificación inválida")
            elif not validar_texto(idioma):
                print("Idioma inválido")
            elif not validar_es_3d(es_3d):
                print("Debe ingresar s o n")
            elif not validar_precio(precio):
                print("Precio inválido")
            elif not validar_cupos(cupos):
                print("Cupos inválidos")
            else:
                es_3d_bool = es_3d.lower() == "s"
                agregado = agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d_bool, precio, cupos, peliculas, cartelera)

                if agregado:
                    print("Película agregada")
                else:
                    print("El código ya existe")

        elif opcion == 5:
            codigo = input("Ingrese código de película: ")
            if eliminar_pelicula(codigo,peliculas,cartelera):
                print("Película eliminada")
            else:
                print("El código no existe")

        else:
            print("Programa finalizado.")
            break


main()