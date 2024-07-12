import json
import os
import funciones



def main():
    inventario = funciones.cargar_inventario()
    while True:
        print("\nSistema de inventario de una Tienda Deportiva.\n -------------BIENVENIDOS-------------")
        print("1) Ingresar producto")
        print("2) Editar producto")
        print("3) Eliminar producto")
        print("4) Listar productos")
        print("5) Salir")
        opcion = input(">> ")

        if opcion == "1":
            funciones.ingresar_producto(inventario)
        elif opcion == "2":
            funciones.editar_producto(inventario)
        elif opcion == "3":
            funciones.eliminar_producto(inventario)
        elif opcion == "4":
            funciones.listar_productos(inventario)
        elif opcion == "5":
            print("Saliendo del programa...")
            funciones.guardar_inventario(inventario)
            break
        else:
            print("Error.")

if __name__ == "__main__":
    main()
