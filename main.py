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
    
# if args.test:
#     teams = list()
#     i = 0
#     while i <100:
#         t = solver.solve_random_search(iters = 300)
#         teams.append(t)
#         i+=1
#     p1 = list()
#     p2 = list()
#     p3 = list()
#     p4 = list()
#     p5 = list()
#     p6 = list()
#     t_score = list()

#     for team in teams:
#         i = 0
#         p1.append(np.sum(team.pokemons.fight_results[team.pokemon_indexes[i]]))
#         i+=1
#         p2.append(np.sum(team.pokemons.fight_results[team.pokemon_indexes[i]]))
#         i+=1
#         p3.append(np.sum(team.pokemons.fight_results[team.pokemon_indexes[i]]))
#         i+=1
#         p4.append(np.sum(team.pokemons.fight_results[team.pokemon_indexes[i]]))
#         i+=1
#         p5.append(np.sum(team.pokemons.fight_results[team.pokemon_indexes[i]]))
#         i+=1
#         p6.append(np.sum(team.pokemons.fight_results[team.pokemon_indexes[i]]))
#         t_score.append(solver.goal_fun(team))
#     p6 = np.array(p6)
#     p5 = np.array(p5)
#     p4 = np.array(p4)
#     p3 = np.array(p3)
#     p2 = np.array(p2)
#     p1 = np.array(p1)
#     t_score = np.array(t_score)
#     fig, ax = plt.subplots(6)
#     x = range(len(p1))
#     ax[0].plot(x, p1, color='yellow')
#     ax[1].plot(x, p2, color='cyan')
#     ax[2].plot(x, p3, color='red')
#     ax[3].plot(x, p4, color='purple')
#     ax[4].plot(x, p5, color='blue')
#     ax[5].plot(x, p6, color='green')
#     plt.show()
