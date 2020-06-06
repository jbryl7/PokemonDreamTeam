import argparse
def get_parser():
    parser = argparse.ArgumentParser(description='PokemonDreamTeam')
    parser.add_argument("-g","--greedy", action='store_const', required=False, const=True, help="greedy")
    parser.add_argument("-t","--test", action='store_const', required=False, const=True, help="test")
    parser.add_argument("-g2", "--greedy2", action='store_const', required=False, const=True, help="greedy with remaining enemies")
    parser.add_argument("-r","--random", action='store_const', required=False, const=True, help="random search")
    parser.add_argument("-i", "--iterations", action='store', required=False, type=int, help="max iterations for random search")
    parser.add_argument("-input", action="store", required=False, type=str, help="Path to file with pokemon info")
    return parser