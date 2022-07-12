from library.EA import *
from library.utils.operator.selection import ElitismSelection
from library.utils.operator.crossover import OX_Crossover
from library.utils.operator.mutation import SwapMutation
from library.model.ga import model
from library.utils.load_data import Load

from argparse import ArgumentParser
import matplotlib.pyplot as plt
import time

if __name__ == "__main__":

    parser = ArgumentParser(add_help=False)
    parser.add_argument("--dataset", type=str)
    parser.add_argument("--num_epoch", default=100, type=int)
    parser.add_argument("--pop_size", default=1000, type=int)
    parser.add_argument("--prob_m", default=0.2, type=float)
    parser.add_argument("--prob_c", default=0.7, type=float)


    param = parser.parse_args()
    print("INFO - DATA:")
    data = Load()
    data(param.dataset)
    print(data)
    print(f"\nGENETIC ALGORITHM: \n\t+ Population: {param.pop_size} individuals\n\t+ Number generations: {param.num_epoch} \
        \n\t+ Probability crossover: {param.prob_c}\n\t+ Probability mutation: {param.prob_m}\n")
    time_begin = time.time()
    ga_model = model()

    ga_model.compile(
        data_loc=param.dataset,
        crossover=OX_Crossover(),
        mutation=SwapMutation(),
        selection=ElitismSelection()
    )

    solution = ga_model.fit(
    num_generations=param.num_epoch,
    num_individuals=param.pop_size,
    prob_crossover=param.prob_c,
    prob_mutation=param.prob_m
    )
    
    print("\n\nFinished:")
    print(solution)
    print(f"Time taken: {round(time.time() - time_begin, 2)}")


    plt.plot(ga_model.res)
    plt.title("Convergence process")
    plt.xlabel("Epoch")
    plt.ylabel("Cost")
    plt.show()