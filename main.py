from solver import *
from input_utils import *


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
    solver.solve_greedy()
if args.greedy2:
    print('greedy with remaining enemies')
    solver.solve_greedy_remaining_enemies()
if args.random:
    iters = 100
    if args.iterations:
        iters = args.iterations
    print("Random search with ", iters, " iterations")
    solver.solve_random_search(iters = iters)
    



