import array

# Algoritmo Optimo ----------
def Optimo(paginas, peticiones, marco):
    # Array vacio para el numero dado de marcos.
    fr = array.array('i', [-1] * marco)
    
    acierto = 0
    for i in range(peticiones):
        found = False
        for j in range(marco):
            if fr[j] == paginas[i]:
                acierto += 1
                found = True
                break

        if found:
            continue


        emptyFrame = False
        for j in range(marco):
            if fr[j] == -1:
                fr[j] = paginas[i]
                emptyFrame = True
                break

        if emptyFrame:
            continue


        farthest = -1
        replaceIndex = -1
        for j in range(marco):
            k = i + 1
            while(k < peticiones):
                if fr[j] == paginas[k]:
                    if k > farthest:
                        farthest = k
                        replaceIndex = j
                    break
                k += 1
            if k == peticiones:
                replaceIndex = j
                break
        fr[replaceIndex] = paginas[i]

    fallos = peticiones - acierto
    print("No. de Fallos: ", fallos)
    return fallos
# ---------------------------


# Algoritmo de Bit de referencia ----------
def Bit_de_referencia(x, array_pg, second_chance, marco):
    for i in range(marco):
        if array_pg[i] == x:
            for j in range(marco):
                if j != i:
                    second_chance[j] = False
            second_chance[i] = True
            return True
    return False

def reemplazo(x, array_pg, second_chance, marco, pointer):
    while True:
        if not second_chance[pointer]:
            array_pg[pointer] = x
            pointer = (pointer + 1) % marco
            return pointer
        second_chance[pointer] = False
        pointer = (pointer + 1) % marco

def aciertos_y_fallos(reference_array, marco):
    pointer = 0
    fallos_pg = 0
    array_pg = [-1] * marco
    second_chance = [False] * marco

    for x in reference_array:
        if not Bit_de_referencia(x, array_pg, second_chance, marco):
            pointer = reemplazo(x, array_pg, second_chance, marco, pointer)
            fallos_pg += 1

    print(f'Total de fallos de página: {fallos_pg}')
    return fallos_pg

secuencia = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0]
aciertos_y_fallos(secuencia, 3)
# -----------------------------------------


# Algoritmo LRU ----------
def LRU(paginas, peticiones, marcos):
    memoria_pg = set()

    # Numeros menos usado
    indexes = {}
    fallos = 0

    for i in range(peticiones):
        if len(memoria_pg) < marcos:

            if paginas[i] not in memoria_pg:
                memoria_pg.add(paginas[i])

                fallos += 1

            indexes[paginas[i]] = i

        else:
            if paginas[i] not in memoria_pg:

                lru = float('inf')
                for page in memoria_pg:
                    if indexes[page] < lru:
                        lru = indexes[page]
                        val = page

                memoria_pg.remove(val)

                memoria_pg.add(paginas[i])

                fallos += 1

            indexes[paginas[i]] = i

    print("fallos", fallos)
    return fallos
# ------------------------

