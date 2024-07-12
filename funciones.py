import json
import os

MAX_PRODUCTOS = 100
INVENTARIO_FILENAME = "inventario.json"

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

def cargar_inventario():
    if os.path.exists(INVENTARIO_FILENAME):
        with open(INVENTARIO_FILENAME, "r") as file:
            data = json.load(file)
            return [Producto(**item) for item in data]
    return []

def guardar_inventario(inventario):
    with open(INVENTARIO_FILENAME, "w") as file:
        json.dump([vars(producto) for producto in inventario], file, indent=4)

def ingresar_producto(inventario):
    if len(inventario) < MAX_PRODUCTOS:
        nombre = input("Ingrese el producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio por favor: "))
        inventario.append(Producto(nombre, cantidad, precio))
    else:
        print("Inventario lleno")

def editar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a editar: ")
    for producto in inventario:
        if producto.nombre == nombre:
            producto.cantidad = int(input("Ingrese la nueva cantidad: "))
            producto.precio = float(input("Ingrese el nuevo precio: "))
            return
    print("Producto no encontrado.")

def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto para borrar por favor: ")
    for i, producto in enumerate(inventario):
        if producto.nombre == nombre:
            del inventario[i]
            print("Producto eliminado.")
            return
    print("No encontrado.")

def listar_productos(inventario):
    for producto in inventario:
        print(producto)