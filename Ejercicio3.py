import random
import search
import sys
import csp

class GeneticAlgorithm_v2():
    def __init__(self, Number_of_queens, max_value):
        ## Numero de reinas, valor maximo ( el numero de pares de reinas que no se atacan, el objetivo es llegar este valor)
        ## y la probabilidad de mutacion.
        self.Number_of_queens=Number_of_queens
        self.max_value=max_value
        self.mutation_probability=0.1

    def value(self, element):
        ## Da valor al elemento dependiendo de su posicion.
        final = 0

        for r1 in range(len(element)):
            for r2 in range(r1 + 1, len(element)):
                c1 = int(element[r1])
                c2 = int(element[r2])
                total_row = r1 - r2
                total_col = c1 - c2
                ## Si no están en la misma
                if ((c1 != c2)and(total_row != total_col)and(total_row != -total_col)):
                    final += 1
        return final

    def mutate(self, element):
        ## Muta el elemento pasado, poniendo en la posicion number1, el numero number2.
        number1 = random.randint(0, Number_of_queens - 1)
        number2 = random.randint(1, Number_of_queens)
        element[number1] = number2
        return element
            
    def procreate(self, parent1, parent2):
        ## Recombina los elementos de ambos padres, generando un numero aleatorio.
        number = random.randint(0, Number_of_queens)
        child = parent1[:number] + parent2[number:]
        return child
    
    def pick_random(self, population, probabilities):
        ## Elije un elemento aleatorio de population.
        values = zip(population, probabilities)
        total = sum(w for c, w in values)
        r = random.uniform(0, total)
        u = 0
        for c, w in zip(population, probabilities):
            if u + w >= r:
                return c
            u += w
        return None


    def genetic_search(self, population, value):
        ## crea una nueva poblacion 
        new_population = []
        ## Añade a elements la division entre el valor que tiene i y el valor maximo
        elements = []
        for i in population:
            elements.append(value(i) / self.max_value)
        ## Va recombinando los elementos aleatoriamente.(La probabilidade de recombinar es 1, para que vaya más rapido)
        for i in range(len(population)):
            child = self.procreate(self.pick_random(population, elements), self.pick_random(population, elements))
            ## Si el numero aleatorio es mayor que la probailidad de mutar, muta y se añade a la nueva poblacion.
            if random.random() < self.mutation_probability:
                child = self.mutate(child)
            new_population.append(child)
            ## Si el valor de child es el max_value, deja de recombinar y mutar.
            if value(child) == self.max_value:
                break
        return new_population

def print_board( board):
        for row in board:
            print (" ".join(row))

def my_genetic_algorithm(problem,Number_of_queens,max_value):


    initial_population=100
    ## Crea un algoritmo genetico problem

    ## Crea una poblacion aleatoria creando elementos entre 1 y Number_of_queens, Number_of_queens veces, init_pop veces.
    population = [[random.randint(1, Number_of_queens) for i in range(Number_of_queens)] for j in range(initial_population)]


    solution = []

    ## Mientras que no esté max_value en population, se sigue buscando.
    keep_going=True
    while keep_going:
        population = problem.genetic_search(population, problem.value)
        for i in population:
            if (max_value == problem.value(i)):
                solution = i
                keep_going=False
                break
       
        
    
    ## Crea la lista y mete el "tablero".
    board = []

   
    for _ in range(Number_of_queens):
        board.append(["-"] * Number_of_queens)
        
    for i in range(Number_of_queens):
        board[Number_of_queens-solution[i]][i]="Q"

    print()
    print("One possible solution: ")
    print()
    print_board(board)
    return solution
  

if __name__ == "__main__":
    
    ## Declara el numero de reinas, el init pop y el maximum value.
    Number_of_queens = 5
    max_value = (Number_of_queens*(Number_of_queens-1))/2
    problem = GeneticAlgorithm_v2(Number_of_queens, max_value)
    solution = my_genetic_algorithm(problem,Number_of_queens,max_value)
    print(solution)