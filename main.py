from solver import *
from input_utils import *
import matplotlib
import matplotlib.pyplot as plt

path_to_data = './data/pokemon.csv'
args = get_parser().parse_args()
if args.input:
    path_to_data = args.input
else:
    print('Using default path to data ', path_to_data)

pokemons = PokemonList().from_file(path_to_data)
solver = Solver(pokemons)

if args.greedy:
    print('greedy')
    solver.show_result(solver.solve_greedy())
if args.greedy2:
    print('greedy with remaining enemies')
    solver.show_result(solver.solve_greedy_remaining_enemies())
if args.random:
    iters = 100
    if args.iterations:
        iters = args.iterations
    print("Random search with ", iters, " iterations")
    solver.show_result(solver.solve_random_search(iters = iters))
if args.test_pokemon_fight:
    p1 = pokemons[0]
    p2 = pokemons[3]
    print(p1.fight_result(p2))
    p1.hits_needed_to_be_defeated2(p2)
    p2.hits_needed_to_be_defeated2(p1)
