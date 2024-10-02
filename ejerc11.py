from cola import Queue

cola_personajes = Queue()

personajes = [
    ("Luke Skywalker", "Tatooine"),
    ("Leia Organa", "Alderaan"),
    ("Han Solo", "Corellia"),
    ("Chewbacca", "Kashyyyk"),
    ("Yoda", "Dagobah"),
    ("Darth Vader", "Tatooine"),
    ("Jar Jar Binks", "Naboo"),
    ("R2-D2", "Naboo"),
    ("C-3PO", "Tatooine")
]

for personaje in personajes:
    cola_personajes.arrive(personaje)

# a. Mostrar los personajes del planeta Alderaan, Endor y Tatooine
def mostrar_planetas_personaje(queue, planets):
    print("Personajes de los planetas:", ", ".join(planets))
    for personaje in queue.get_elements():
        if personaje[1] in planets:
            print(f"{personaje[0]} del planeta {personaje[1]}")
    print()

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
def mostrar_planeta_natal(queue, names):
    for character in queue.get_elements():
        if character[0] in names:
            print(f"{character[0]} es del planeta {character[1]}")
    print()

# c. Insertar un nuevo personaje antes del maestro Yoda
def insertar_antes_yoda(queue, new_character):
    elements = queue.get_elements()
    index = None
    for i, character in enumerate(elements):
        if character[0] == "Yoda":
            index = i
        
    if index is not None:
        elements.insert(index, new_character)
    print(f"Se ha insertado a {new_character[0]} antes de Yoda.")

# d. Eliminar el personaje ubicado después de Jar Jar Binks
def eliminar_antes_jarjar(queue):
    elements = queue.get_elements()
    index = None
    for i, character in enumerate(elements):
        if character[0] == "Jar Jar Binks":
            index = i
        
    if index is not None and index + 1 < len(elements):
        removed_character = elements.pop(index + 1)
        print(f"Se ha eliminado a {removed_character[0]} que estaba después de Jar Jar Binks.")
    else:
        print("No hay ningún personaje después de Jar Jar Binks para eliminar.")



mostrar_planetas_personaje(cola_personajes, ["Alderaan", "Endor", "Tatooine"])


mostrar_planeta_natal(cola_personajes, ["Luke Skywalker", "Han Solo"])


new_character = ("Obi-Wan Kenobi", "Stewjon")
insertar_antes_yoda(cola_personajes, new_character)


eliminar_antes_jarjar(cola_personajes)

print()




