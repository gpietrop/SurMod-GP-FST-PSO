import numpy as np
import math
from math import sqrt
from sklearn.metrics import mean_squared_error

import fstpso
from fstpso import FuzzyPSO

from print import *
from eval import make_function
from hyperparam import *

if function_name == "ackley":
    if dim == 1: 
        from benchmark_function import ackley as benchmark_fun
    if dim == 2:
        from benchmark_function import ackley_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import ackley_3d as benchmark_fun

if function_name == "alpine":
    if dim == 1:
        from benchmark_function import alpine as benchmark_fun
    if dim == 2:
        from benchmark_function import alpine_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import alpine_3d as benchmark_fun

if function_name == "griewank":
    if dim == 1:
        from benchmark_function import griewank as benchmark_fun
    if dim == 2:
        from benchmark_function import griewank_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import griewank_3d as benchmark_fun

if function_name == "michalewicz":
    if dim == 2:
        from benchmark_function import michalewicz_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import michalewicz_3d as benchmark_fun

if function_name == "rastring":
    if dim == 1:
        from benchmark_function import rastring as benchmark_fun
    if dim == 2:
        from benchmark_function import rastring_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import rastring_3d as benchmark_fun

if function_name == "rosenbrock":
    if dim == 2:
        from benchmark_function import rosenbrock_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import rosenbrock_3d as benchmark_fun

if function_name == "schwefel":
    if dim == 1:
        from benchmark_function import schwefel as benchmark_fun
    if dim == 2:
        from benchmark_function import schwefel_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import schwefel_3d as benchmark_fun

if function_name == "shubert":
    if dim == 1:
        from benchmark_function import shubert as benchmark_fun
    if dim == 2:
        from benchmark_function import shubert_2d as benchmark_fun

if function_name == "vincent":
    if dim == 1:
        from benchmark_function import vincent as benchmark_fun
    if dim == 2:
        from benchmark_function import vincent_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import vincent_3d as benchmark_fun

if function == "xinshe":
    if dim == 1:
        from benchmark_function import xinshe as benchmark_fun
    if dim == 2:
        from benchmark_function import xinshe_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import xinshe_3d as benchmark_fun


def strong_fitness(prg, n=number_interpolation_point):
    """
    Fitness combined: we want both that the minimum of the approx program coincide with the minimum of the function and
    that the function and the approx program have some points in common (here n)
    :param prg: program that approximate the function
    :param n: number of point for the rmse computation
    :return: fitness
    """
    try:
        x_coord_best = fst_pso_loss(prg)
    except Exception:
        return math.inf
    if not x_coord_best:
        return math.inf
    if not (interval[0][0] < x_coord_best[0] < interval[0][1] and interval[0][0] < x_coord_best[1] < interval[0][1]):
        return math.inf
    y_benchmark_function = benchmark_fun(x_coord_best)

    points = [[point] for point in np.linspace(interval[0][0], interval[0][-1], n)]

    approx_fun = make_function(prg)

    y_true = [benchmark_fun(point) for point in points]
    y_true.append(y_benchmark_function)

    try:
        y_pred = [approx_fun(point) for point in points]
    except Exception:
        return math.inf
    try:
        y_pred.append(approx_fun(x_coord_best))
    except Exception:
        return math.inf

    try:
        rmse = mean_squared_error(y_true, y_pred)
    except Exception:
        return math.inf

    return y_benchmark_function + rmse


def strong_fitness_2d(prg, n=number_interpolation_point):
    """
    Fitness combined: we want both that the minimum of the approx program coincide with the minimum of the function and
    that the function and the approx program have some points in common (here n)
    :param prg: program that approximate the function
    :param n: number of point for the rmse computation
    :return: fitness
    """
    try:
        x_coord_best = fst_pso_loss(prg)
    except Exception:
        return math.inf
    if not x_coord_best or len(x_coord_best) < 2:
        return math.inf
    if not (interval[0][0] < x_coord_best[0] < interval[0][1] and interval[0][0] < x_coord_best[1] < interval[0][1]):
        return math.inf
    try:
        y_benchmark_function = benchmark_fun(x_coord_best[0], x_coord_best[1])
    except Exception:
        return math.inf

    x1_points = [point for point in np.linspace(interval[0][0], interval[0][-1], n)]
    x2_points = [point for point in np.linspace(interval[0][0], interval[0][-1], n)]

    approx_fun = make_function(prg)

    y_true = [benchmark_fun(x1, x2) for x1 in x1_points for x2 in x2_points]
    y_true.append(y_benchmark_function)

    try:
        y_pred = [approx_fun([x1, x2]) for x1 in x1_points for x2 in x2_points]
    except Exception:
        return math.inf
    try:
        y_pred.append(approx_fun(x_coord_best))
    except Exception:
        return math.inf

    try:
        rmse = mean_squared_error(y_true, y_pred)
    except Exception:
        return math.inf

    return y_benchmark_function + rmse


def strong_fitness_3d(prg, n=number_interpolation_point):
    """
    Fitness combined: we want both that the minimum of the approx program coincide with the minimum of the function and
    that the function and the approx program have some points in common (here n)
    :param prg: program that approximate the function
    :param n: number of point for the rmse computation
    :return: fitness
    """
    try:
        x_coord_best = fst_pso_loss(prg)
    except Exception:
        return math.inf
    if not x_coord_best or len(x_coord_best) < 2:
        return math.inf
    for coord_best in x_coord_best: 
        if not interval[0][0] < coord_best < interval[0][1]:
            return math.inf
        
    try:
        y_benchmark_function = benchmark_fun(x_coord_best[0], x_coord_best[1], x_coord_best[2])
    except Exception:
        return math.inf

    '''
    x1_points = [point for point in np.linspace(interval[0][0], interval[0][-1], n)]
    x2_points = [point for point in np.linspace(interval[0][0], interval[0][-1], n)]
    x3_points = [point for point in np.linspace(interval[0][0], interval[0][-1], n)]

    approx_fun = make_function(prg)

    y_true = [benchmark_fun(x1, x2, x3) for x1 in x1_points for x2 in x2_points for x3 in x3_points]
    y_true.append(y_benchmark_function)

    try:
        y_pred = [approx_fun([x1, x2, x3]) for x1 in x1_points for x2 in x2_points for x3 in x3_points]
    except Exception:
        return math.inf
    try:
        y_pred.append(approx_fun(x_coord_best))
    except Exception:
        return math.inf

    try:
        rmse = mean_squared_error(y_true, y_pred)
    except Exception:
        return math.inf
    '''

    return y_benchmark_function  # + rmse


def fst_pso_loss(prg):
    """
    :param prg: individual of the population (program)
    :param dim: dimension of the space (also called D)
    :param interval: interval of the problem (insert a list like: [[-10, 10]])
    :return: coordinates relative to the minimum of prg
    """
    blockPrint()
    FP = FuzzyPSO()
    FP.set_search_space(interval * dim)
    FP.set_fitness(make_function(prg))
    result = FP.solve_with_fstpso()
    enablePrint()
    return result[0].X  # the .X transfrom the Particle structure into a list
