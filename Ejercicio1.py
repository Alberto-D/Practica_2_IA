import random
import search
import sys
import csp


class NQueensCSP_v2():
    def __init__(self, N):
        self.N = N

    def initial(self):
        lista = []
        ## Crea una lista, le añade N elementos aleatorios entre 0 y N y la devuelve.
        for i in range(self.N):
            lista.append(random.randrange(self.N))
        
        return lista

    def conflict(self, row1, col1, row2, col2):
        ## Comprueba si estan en la misma fila, columna, o diagonal, si lo está devuelve 1, el conflicto, si no, 0.
        if(row1 == row2 or col1 == col2 or row1 - col1 == row2 - col2 or row1 + col1 == row2 + col2):
            return 1
        return 0

    def result(self, state, row, col):
        ## Crea newState vacia y copia state en ella.
        newState = [None] * len(state)
        for i in range(0, len(state)):
            newState[i] = state[i]
        ## Compara la columna y lo que hay en row en newState, si es distinto lo copio y devuelvo newState, para tener todos los estados.
        if  col != newState[row]:
            newState[row] = col
            return newState
        return None

    def child_node(self, row, state, lista):
        for col in range(self.N):
            elem = self.result(state, row, col)
            ## Si el elemento es distinto a None, lo añado a la lista.
            if elem != None:
                lista.append(elem)
        return lista

    def value(self, current):
        num_conflicts = 0
        ## Comprueba el numero de conflictos en el estado actual.
        for (r1, c1) in enumerate(current):
            for (r2, c2) in enumerate(current):
                if (r1, c1) != (r2, c2):
                    num_conflicts += self.conflict(r1, c1, r2, c2)
        ## Si hay 0 confilctos, devuelve 1, si no -1.
        if num_conflicts == 0:
            return 1
        return -1

    def expand(self, state):
        lista = []
        # Mira cada elemento de la lista y la expande añadiendolo.
        for row in range(self.N):
            lista = self.child_node(row, state, lista)
        return lista


def my_hill_climbing(problem):
    current = problem.initial()
    num=0
    print("Inicial:", current)
    while True:
         ## Si value es 1, es decir, si en current hay 0 conflictos, acabo.
        if problem.value(current) == 1:
            break
        ## Mide los pasos que ha tardado en llegar a la solucion.
        num+=1
        ## Expande el problema.
        neighbours = problem.expand(current)
        ## Si no hay neighbours, salgo.
        if not neighbours:
            break
        ## Elije una de sus casillas vecinas, entras las que tengan el valor mas alto, si es el mismo, se elije aleatoriamente.
        neighbour = search.argmax_random_tie(neighbours, key=lambda node: problem.value( current))
       
        ## Si no, current es ahora neighbour.
        current = neighbour
    
    return current,num


if __name__ == "__main__":
    problem = NQueensCSP_v2(5)
    solution, steps = my_hill_climbing(problem)
    print("Solution: ",solution, " took ", steps, " steps.")