from cola import Queue

cola_personajes = Queue()


personajes = [
    ("Tony Stark", "Iron Man", "M"),
    ("Steve Rogers", "Capitán América", "M"),
    ("Natasha Romanoff", "Black Widow", "F"),
    ("Carol Danvers", "Capitana Marvel", "F"),
    ("Scott Lang", "Ant-Man", "M"),
    ("Wanda Maximoff", "Scarlet Witch", "F"),
    ("Peter Parker", "Spider-Man", "M"),
    ("Stephen Strange", "Doctor Strange", "M")
]


for personaje in personajes:
    cola_personajes.arrive(personaje)

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
def nombre_capitana_marvel(queue, nombre):
    for personaje in queue.get_elements():
        if personaje[1] == nombre:
            print(f"El nombre de {nombre} es {personaje[0]}")
            return
    print(f"No se encontró ningún personaje con el nombre {nombre}")

# b. Mostrar los nombres de los superhéroes femeninos
def nombre_femenino(queue):
    print("Superhéroes femeninos:")
    for personaje in queue.get_elements():
        if personaje[2] == "F":
            print(f"{personaje[1]}")
    print()

# c. Mostrar los nombres de los personajes masculinos
def nombre_masculino(queue):
    print("Personajes masculinos:")
    for personaje in queue.get_elements():
        if personaje[2] == "M":
            print(f"{personaje[0]}")
    print()

# d. Determinar el nombre del superhéroe del personaje Scott Lang
def nombre_superheroe_scott(queue, nombre):
    for personaje in queue.get_elements():
        if personaje[0] == nombre:
            print(f"El superhéroe de {nombre} es {personaje[1]}")
            return()
    print(f"No se encontró ningún superhéroe con el personaje {nombre}.")

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
def datos_nombres_s(queue, letra):
    print(f"Personajes o superhéroes cuyos nombres comienzan con la letra '{letra}':")
    for personaje in queue.get_elements():
        if personaje[0].startswith(letra) or personaje[1].startswith(letra):
            print(f"{personaje[0]}, {personaje[1]}, {personaje[2]}")
    print()

# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
def encontrar_carol_danvers(queue, nombre):
    for personaje in queue.get_elements():
        if personaje[0] == nombre:
            print(f"{nombre} se encuentra en la cola y su nombre de superhéroe es {personaje[1]}")
            return
    print(f"{nombre} no se encuentra en la cola.")




nombre_capitana_marvel(cola_personajes, "Capitana Marvel")


nombre_femenino(cola_personajes)


nombre_masculino(cola_personajes)


nombre_superheroe_scott(cola_personajes, "Scott Lang")


datos_nombres_s(cola_personajes, "S")


encontrar_carol_danvers(cola_personajes, "Carol Danvers")

