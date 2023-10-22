from typing import Tuple

from pyvrp import read, ProblemData
from pyvrp._pyvrp import Solution, RandomNumberGenerator, CostEvaluator
from pyvrp.search import LocalSearch, NODE_OPERATORS, ROUTE_OPERATORS, NeighbourhoodParams, compute_neighbours
from utils.CustomSREX import selective_route_exchange as CustomSREX


def get_category_label(
        offspring_ls: Solution,
        offspring_srex: Solution,
        couple: Tuple[Solution, Solution],
        cost_evaluator: CostEvaluator
):
    """
    Creates category value given offspring and parents

    Categories:
        0: offspring is fully equal to on of the parents
        1: if offspring is infeasible
        2: offspring is worse in cost then best parents
        3: offspring is equal in cost to best parent
        4: offspring is better in cost then best parent

    """

    parent1, parent2 = couple
    ls_cost = cost_evaluator.penalised_cost(offspring_ls)
    parent1_cost = cost_evaluator.penalised_cost(parent1)
    parent2_cost = cost_evaluator.penalised_cost(parent2)

    if ls_cost < min(parent1_cost, parent2_cost):
        return 4

    if offspring_srex == parent1 or offspring_srex == parent2 or offspring_ls == parent1 or offspring_ls == parent2:
        return 0

    if not offspring_ls.is_feasible():
        return 1

    if ls_cost > min(parent1_cost, parent2_cost):
        return 2
    if ls_cost == min(parent1_cost, parent2_cost):
        return 3


    raise "Solution has no category?"


def solve_srex_options(
        data: ProblemData,
        seed: int,
        couple: Tuple[Solution, Solution],
        idx: Tuple[int, int],
        couple_id: int,
        capP: int,
        twP: int,
        moves: int,
):
    rng = RandomNumberGenerator(seed=seed)

    nb_params = NeighbourhoodParams(nb_granular=20)
    neighbours = compute_neighbours(data, nb_params)
    ls = LocalSearch(data, rng, neighbours)

    for op in NODE_OPERATORS:
        ls.add_node_operator(op(data))

    for op in ROUTE_OPERATORS:
        ls.add_route_operator(op(data))

    cost_evaluator = CostEvaluator(capacity_penalty=capP, tw_penalty=twP)

    offspring_srex = CustomSREX(couple, data, cost_evaluator, idx, moves)
    offspring_ls = ls.search(offspring_srex, cost_evaluator)

    parent1, parent2 = couple

    # get Improvement of cost
    ls_cost = cost_evaluator.penalised_cost(offspring_ls)
    parent1_cost = cost_evaluator.penalised_cost(parent1)
    parent2_cost = cost_evaluator.penalised_cost(parent2)
    improv_value = min(parent1_cost, parent2_cost) - ls_cost

    categ_value = get_category_label(offspring_ls=offspring_ls, offspring_srex=offspring_srex, couple=couple,
                                     cost_evaluator=cost_evaluator)

    return improv_value, categ_value


