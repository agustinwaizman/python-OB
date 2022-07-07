items = input("introduce paises separados por comas: ")

paises = [pais for pais in items.split(",")]

print(", ".join(sorted(list(set(paises)))))