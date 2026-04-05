import random

def sorteo(names_set):
    names = list(names_set)
    if len(names) < 3:
        print("Se necesitan al menos 3 personas.")
        return
    
    targets = names.copy()
    random.shuffle(targets)
    
    invisible = {}
    for i in range(len(names)):
        giver = targets[i]
        receiver = targets[(i + 1) % len(targets)]
        invisible[giver] = receiver

    print("Sorteo de amigo invisible: ")
    for key, value in invisible.items():
        print(f'{key} → {value}')