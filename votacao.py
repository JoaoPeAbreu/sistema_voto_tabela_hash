registro = {}

votos = {}

def vote(idvoto, candidato):
    if idvoto in registro:
        return "Erro: Eleitor já votou."
    else:
        registro[idvoto] = candidato
        votos[candidato] = votos.get(candidato, 0) + 1
        return f"Voto registrado para {candidato}!"

def show_results():
    print("Resultados da eleição:")
    for candidato, count in votos.items():
        print(f"{candidato}: {count} votos")


print(vote("123", "Alice"))
print(vote("123", "Bob"))
print(vote("456", "Bob"))
print(vote("789", "Alice"))
show_results()