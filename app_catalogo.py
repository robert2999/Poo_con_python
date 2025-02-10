from peli import pelicula
from catalogo_peli import CatalogoPelicula
print("**** App catalogo de pelicula***")
opcion=None
while opcion!=4: 
    try:
        print("""
        opciones:
        1.Agregar pelicula
        2.Listar peliculas
        3.Eliminar catalogo de peliculas
        4.Salir 
""")
        opcion=int(input("Escriba la opcion :(1-4)"))
        if opcion==1:
            nombre_pelicula=input("Ingrese el nombre de la pelicula: ")
            pelic=pelicula(nombre_pelicula)
            CatalogoPelicula.agregar_peliculas(pelic)
        elif opcion==2:
            CatalogoPelicula.listar_peliculas()
        elif opcion==3:
            CatalogoPelicula.eliminar_catalogo()
    except Exception as e: 
        print(f"Ocurrio un valor de error {e}")   
        opcion=None