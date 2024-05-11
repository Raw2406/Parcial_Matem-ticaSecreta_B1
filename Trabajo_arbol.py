from graphviz import Digraph

########################################################################################################################################
def CARATULA():
    print(" ")
    print(" ")
    print("               ///                 UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS                ///")
    print(" ")
    print("                                       Segundo Informe del Trabajo Final                             ")
    print(" ")
    print("                                            iNFORMES DE ARBOLES TB1                             ")
    print(" ")
    print("               Seccion: SV33")
    print(" ")
    print("               Curso: Matematica Discreta")
    print(" ")
    print("               Profesor: Antonio Marcos Medina Martínez")
    print(" ")
    print("               Integrantes: - Anjely Luciana, Geronimo Quispe      (U20231F162)")
    print("                            - Natalie Vanessa Gaspar Chumbile      (U202216936)")
    print("                            - Malmaceda Campana, Diego Alonso      (U20231B037)")
    print("                            - Sanchez Heredia, Stefano Lucarelly   (U202314926)")
    print("                            - Soto Ccopa Orlando Gabriel           (U202314275)")
    print(" ")
    print(" ")
    print( "                                                    1                      " )
    print( "                                                  1 1                      " )
    print( "                                                1 1 1                      " )
    print( "                                      1         1 1 1               1      " )
    print( "                                    1 1       1 1 1 1 1             1 1    " )
    print( "                                  1 1         1 1 1 1 1 1             1 1  " )
    print( "                                  1 1         1 1 1 1 1 1 1           1 1  " )
    print( "                                1 1 1         1 1 1 1 1 1 1           1 1 1" )
    print( "                                1 1 1         1 1 1 1 1 1 1 1         1 1 1" )
    print( "                                1 1 1           1 1 1 1 1 1 1         1 1 1" )
    print( "                                1 1 1           1 1 1 1 1 1 1         1 1 1" )
    print( "                                1 1 1 1           1 1 1 1 1 1       1 1 1 1" )
    print( "                                1 1 1 1             1 1 1 1 1       1 1 1 1" )
    print( "                                1 1 1 1 1             1 1 1 1     1 1 1 1 1" )
    print( "                                1 1 1 1 1 1           1 1 1 1 1 1 1 1 1 1 1" )
    print( "                                  1 1 1 1 1 1 1       1 1 1 1 1 1 1 1 1 1  " )
    print( "                                  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1  " )
    print( "                                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1    " )
    print( "                                      1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1      " )
    print( "                                        1 1 1 1 1 1 1 1 1 1 1 1 1 1        " )
    print( "                                          1 1 1 1 1 1 1 1 1 1 1 1          " )
    print( "                                                1 1 1 1 1 1                " )
    print(" ")
    print(" ")
    print("                                                   2024-01                             ")
    print(" ")
    print(" ")

CARATULA()  
########################################################################################################################################

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def construir_arbol(n_elementos, n_hijos):
    nodos = [Nodo(chr(65 + i)) for i in range(n_elementos)]
    arbol_ext = []  # Lista para almacenar las conexiones del árbol en extensión

    for i in range(n_elementos):
        for j in range(n_hijos):
            hijo_index = i * n_hijos + j + 1
            if hijo_index < n_elementos:
                nodos[i].hijos.append(nodos[hijo_index])
                # Agregar la conexión al árbol en extensión
                arbol_ext.append((nodos[i].valor, nodos[hijo_index].valor))

    return nodos[0], arbol_ext

def mostrar_arbol_extenso(arbol_ext):
    print("Árbol en extensión:")
    for conexion in arbol_ext:
        print(conexion)

def dibujar_digrafo(arbol_ext):
    dot = Digraph(comment='Árbol')
    for u, v in arbol_ext:
        dot.node(str(u), str(u))
        dot.node(str(v), str(v))
        dot.edge(str(u), str(v))
    dot.render('output/tree.gv', view=True)
    return dot

class BinaryNode:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def construir_arbol_binario(root: Nodo):
    arbol_ext = []  # Lista para almacenar las conexiones del árbol en extensión
    queue = []
    binary_root = BinaryNode(root.valor)
    queue.append((root, binary_root))
    while(len(queue) > 0):
        t, b = queue.pop(0)
        if (len(t.hijos) == 0):
            continue
        b.izq = BinaryNode(t.hijos[0].valor)
        cn = b.izq
        arbol_ext.append((b.valor, b.izq.valor))
        queue.append((t.hijos[0], cn))
        for i in range(1, len(t.hijos)):
            cn.der = BinaryNode(t.hijos[i].valor)
            arbol_ext.append((cn.valor, cn.der.valor))
            cn = cn.der
            queue.append((t.hijos[i], cn))

    return binary_root, arbol_ext

def preorden(node):
    if node is not None:
        print(node.valor, end=" ")
        preorden(node.izq)
        preorden(node.der)

def inorden(node):
    if node is not None:
        inorden(node.izq)
        print(node.valor, end=" ")
        inorden(node.der)

def postorden(node):
    if node is not None:
        postorden(node.izq)
        postorden(node.der)
        print(node.valor, end=" ")

def main():
    print("**********************************************************************")
    print(" ")
    print("BIENVENIDO INGRESE LOS SIGUIENTES DATOS PARA LA CREACION DE SU ARBOL")
    print(" ")
    print("**********************************************************************")
    print(" ")
    n_elementos = int(input("Ingrese la cantidad de elementos del árbol (entre 10 y 15): "))
    if n_elementos < 10 or n_elementos > 15:
        print("El número de elementos debe estar entre 10 y 15.")
        return

    tipo_arbol = int(input("Ingrese la cantidad de hijos o el tipo de árbol (2 a 4): "))
    if tipo_arbol < 2 or tipo_arbol > 4:
        print("El tipo de árbol debe estar entre 2 y 4.")
        return

    while True:
        print("**********************************************************************")
        print(" ")
        print("Seleccione una opcion:")
        print(" ")
        print("1. Presentar los elementos de T por extensión.")
        print("2. Trazar su dígrafo.")
        print("3. Determinar su árbol B(T) y elementos por extensión.")
        print("4. Determinar el recorrido en preorden, inorden, postorden")
        print("5. Salir")
        print(" ")

        opcion = input("Ingrese el número de la opción que desea: ").strip()
        print(" ")
        print("**********************************************************************")
        print(" ")

        if opcion == "1":
            arbol, arbol_ext = construir_arbol(n_elementos, tipo_arbol)
            mostrar_arbol_extenso(arbol_ext)

        elif opcion == "2":
            arbol, arbol_ext = construir_arbol(n_elementos, tipo_arbol)
            dibujar_digrafo(arbol_ext)

        elif opcion == "3":
            arbol, arbol_ext = construir_arbol(n_elementos, tipo_arbol)
            bt, ext = construir_arbol_binario(arbol)
            mostrar_arbol_extenso(ext)
            dibujar_digrafo(ext)

        elif opcion == "4":
            # Aquí deberías llamar a la función que determina el recorrido en preorden, inorden, postorden
            arbol, arbol_ext = construir_arbol(n_elementos, tipo_arbol)
            bt, ext = construir_arbol_binario(arbol)
            print("Recorrido en Preorden:")
            preorden(bt)
            print("\nRecorrido en Inorden:")
            inorden(bt)
            print("\nRecorrido en Postorden:")
            postorden(bt)
            print("\n")
            pass

        elif opcion == "5":
            print("Gracias por usar nuestro programa")
            break  # Sale del bucle while y termina el programa

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
