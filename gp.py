import enum
import math
import random

import numpy as np

from hyperparam import *
from print import *
from eval import opcodes, make_function
from fitness import fst_pso_loss
from plot_function import plot_prg, plot_prg_2d

if fitn == "strong_fitness_4":
    from fitness import strong_fitness_4 as fit
if fitn == "strong_fitness_2d":
    from fitness import strong_fitness_2d as fit
if fitn == "strong_fitness_contour_2d":
    from fitness import strong_fitness_contour_2d as fit
if fitn == "fitness_2d":
    from fitness import fitness_2d as fit
if fitn == "strong_fitness_3d":
    from fitness import strong_fitness_3d as fit
if fitn == "strong_fitness_4d":
    from fitness import strong_fitness_4d as fit
if fitn == "strong_fitness_5d":
    from fitness import strong_fitness_5d as fit

snap = 1
if function_name == "griewank":
    max_fit = 10 ** 4
    min_con, max_con = -500, 500
elif function_name == "rosenbrock":
    max_fit = 10 ** 6
elif function_name == "rosenbrock" or (function_name == "schwefel" and flag_plot == 1):
    max_fit = 10 ** 7
else:
    max_fit = 10 ** 3
    min_con, max_con = -10, 10

special_op_func = ["shubert", "michalewicz", "schwefel", "vincent", "rosenbrock"]


def random_op_small():
    if random.random() < 0.5:  # 0.5
        op = random.randint(-5, 5)
    else:
        op = random.uniform(0, 1)
        op = round(op, 1)

    return op


def random_op_very_small():
    rnd = random.random()
    if rnd < 0.33:  # 0.5
        op = random.randint(-3, 3)
    elif 0.33 < rnd < 0.66:
        op = random.uniform(0, 1)
        op = round(op, 1)
    else:
        op = random.uniform(0, 1)
        op = round(op, 1) * 0.1

    return op


def random_program_attention(n):
    flag = 0
    while not flag:
        prg = []
        func = list(opcodes)
        for i in range(0, n):
            if random.random() < 0.5:  # 0.5
                op = random.choice(func)
            else:
                if function_name in special_op_func:
                    op = random_op_very_small()
                else:
                    op = random.randint(min_con, max_con)  # (-2, 2)
            prg.append(op)
        fit_prg = fit(prg)
        if fit_prg and fit_prg < max_fit:
            enablePrint()
            print("program find with fitness :" + str(fit_prg))
            flag = 1
    return prg


def tournament_selection(fit, pop, t_size=4):
    tournament = random.choices(pop, k=t_size)
    return min(tournament, key=fit)


def two_points_crossover_attention(x, y):
    flag = 0
    max_number_combination = 10
    numb_combination = 0
    while not flag:
        numb_combination += 1
        k1 = random.randint(0, len(x) - 1)
        k2 = random.randint(k1, len(x) - 1)
        h1 = random.randint(0, len(y) - 1)
        h2 = random.randint(h1, len(y) - 1)
        of1 = x[0:k1] + y[h1:h2] + x[k2:]
        of2 = y[0:h1] + x[k1:k2] + y[h2:]

        if len(of1) > max_dim_prg:
            of1 = of1[:max_dim_prg]
        if len(of2) > max_dim_prg:
            of2 = of2[:max_dim_prg]

        fit_of1 = fit(of1)
        fit_of2 = fit(of2)
        if fit_of1 and fit_of2 and fit_of1 < max_fit and fit_of2 < max_fit:
            flag = 1
        if numb_combination == max_number_combination:
            return x, y
    return of1, of2


def mutation_attention(x, p_m):
    flag = 0
    max_number_combination = 10
    numb_combination = 0

    def change(b):
        if random.random() < p_m:
            if random.random() < 0.5:  # 0.5
                op = random.choice(list(opcodes))
            else:
                if function_name in special_op_func:
                    op = random_op_very_small()
                else:
                    op = random.randint(min_con, max_con)  # (-2, 2)
            return op
        else:
            return b

    while not flag:
        mutated_prg = [change(b) for b in x]

        fit_m = fit(mutated_prg)
        if fit_m and fit_m < max_fit:
            flag = 1
        if numb_combination == max_number_combination:
            return x
    return mutated_prg


def linear_GP(fit, pop_size=100, n_iter=100, dim_prg=10, dire=None, run=1):
    external_dire = dire
    dire = dire + str(run) + "/"
    if not os.path.exists(dire):
        os.mkdir(dire)
    f, f_loss, f_argmin = open(dire + "res.txt", "w"), open(dire + "loss.txt", "w"), open(dire + "argmin.txt", "w")
    f_final_argmin, f_resume_argmin, f_resume_loss = open(dire + "argmin_final.txt", "w"), open(
        external_dire + "argmins.txt", "w"), open(external_dire + "fitness.txt", "w")
    p_m = 0.2
    pop = [random_program_attention(dim_prg) for _ in range(0, pop_size)]  # 10
    best = random_program_attention(dim_prg)  # []
    fit_best = fit(best)
    for i in range(0, n_iter):
        if i > 0:
            pop.append(best)

        pop = list(dict.fromkeys([tuple(el) for el in pop]))
        pop = [list(el) for el in pop]

        selected = [tournament_selection(fit, pop) for _ in range(0, pop_size)]
        pairs = zip(selected, selected[1:] + [selected[0]])
        offsprings = []
        for x, y in pairs:
            of1, of2 = two_points_crossover_attention(x, y)
            offsprings.append(of1)
            offsprings.append(of2)

        pop = [mutation_attention(x, p_m) for x in offsprings]
        pop.append(best)

        enablePrint()
        candidate_best = min(pop, key=fit)

        if fit(candidate_best) < fit_best:
            best = candidate_best
            fit_best = fit(best)

        try:
            argmin_best = fst_pso_loss(best)
        except Exception:
            print("not able to compute argmin within fst-pso")
            argmin_best = [math.inf, math.inf]

        print(f"GEN: {i} \t best individual: \t {best}")
        f.write(f"GEN: {i} \t best individual: \t {best}\n")

        print(f"GEN: {i} \t best fitness: \t {fit_best}")
        f.write(f"GEN: {i} \t best fitness: \t {fit_best}\n")

        print(f"GEN: {i} \t argmin best prg: \t {argmin_best}\n")
        f.write(f"GEN: {i} \t argmin best prg: \t {argmin_best}\n")

        f_loss.write(f"{fit_best}\n")
        f_argmin.write(f"{argmin_best}\n")

        if dim < 2:
            x = np.linspace(interval[0][0], interval[0][1], 10001)
            if dire and i % snap == 0:
                plot_prg(best, x, dire, i)
        if dim == 2 and flag_plot == 1:
            if dire and i % snap == 0:
                plot_prg_2d(best, dire, i)

    f_final_argmin.write(f"{argmin_best}")
    f_resume_argmin.write(f"{argmin_best}\n")
    f_resume_loss.write(f"{fit_best}\n")

    f.close()
    f_loss.close()
    f_argmin.close()
    f_final_argmin.close()
    f_resume_argmin.close()
    f_resume_loss.close()

    return best
