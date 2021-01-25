import random
import search
import sys
import csp

def best_first_graph_search(problem, f):
    ## Esta es la funcion sacada del codigo https://github.com/aimacode/aima-python/blob/668a2fb0bcd28b4963648c1425f904baa3826a8f/search.py#L260  y adaptada para el ejercicio.

    ## Comienza la busqueda, guarda f y coje el nodo inical y crea frontier con la minima f(x) y le añade el primer nodo.
    f = search.memoize(f, 'f')
    node = search.Node(problem.initial)
    frontier = search.PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    # Mientras se pueda, saca el ultimo elemento de frontier, comrpueba si se ha cumplido la meta.
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            ## Si se ha cumplido la meta, avisa y acaba el programa devulviendo el nodo en el que se cumple.
            print(len(explored), " nodos se han expnadido y", len(frontier), " sigue en la frontera.")
            return node
        ## Si no se cumple añade el nodo a la lista de explorados.
        explored.add(node.state)
        ## Tras esto, expande el problema alrededor de ese nodo, comprobando si ya ha exploado los nodos que lo rodean y si estan en frontier.
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    ## Si no ha encontrado la meta, devuelve None.
    return None


def astar_search(problem, h=None):
    ## Esta es la funcion sacada del codigo https://github.com/aimacode/aima-python/blob/master/search.py#L415 y adaptada para el ejercicio 

    ## Guarda en h.
    h = search.memoize(h or problem.h, 'h')
    ## Deposita en solution la solucion.
    solution = best_first_graph_search(problem, lambda n: n.path_cost + h(n))
    return solution


if __name__ == "__main__":
    ## Creo una instancia de Nreinas (el tablero por decirlo así).
    problem=search.NQueensProblem(4)
    ##  LLamo al algoritmo A* para que lo solucione.
    solution = astar_search(problem, h=None)
    print(solution)