import numpy as np


def ackley(x):
    D = len(x)
    y = 20 + np.e - 20 * np.exp((-0.2 * np.sqrt(1 / D * np.sum([x[i] ** 2 for i in range(D)])))) \
        - np.exp(1 / D * np.sum([np.cos(2 * np.pi * x[i]) for i in range(D)]))
    return y


def ackley_2d(x, y):
    return 20 + np.e - 20 * np.exp((-0.2 * np.sqrt(1 / 2 * (x ** 2 + y ** 2)))) - np.exp(
        1 / 2 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)))


def ackley_3d(x, y, z):
    return 20 + np.e - 20 * np.exp((-0.2 * np.sqrt(1 / 3 * (x ** 2 + y ** 2 + z ** 2)))) - np.exp(
        1 / 3 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y) + np.cos(2 * np.pi * z)))


def alpine(x):
    D = len(x)
    y = np.sum([(np.abs(x[i] * np.sin(x[i]) + 0.1 * x[i])) for i in range(D)])
    return y


def alpine_2d(x, y):
    return np.abs(x * np.sin(x) + 0.1 * x) + np.abs(y * np.sin(y) + 0.1 * y)


def alpine_3d(x, y, z):
    return np.abs(x * np.sin(x) + 0.1 * x) + np.abs(y * np.sin(y) + 0.1 * y) + np.abs(z * np.sin(z) + 0.1 * z)


def alpine_5d(x1, x2, x3, x4, x5):
    return np.abs(x1 * np.sin(x1) + 0.1 * x1) + np.abs(x2 * np.sin(x2) + 0.1 * x2) + np.abs(x3 * np.sin(x3) + 0.1 * x3) \
           + np.abs(x4 * np.sin(x4) + 0.1 * x4) + np.abs(x5 * np.sin(x5) + 0.1 * x5)


def griewank(x):
    D = len(x)
    y = 1 / 4000 * np.sum([x[i] ** 2 for i in range(D)]) - np.prod(
        [(np.cos(x[i] / np.sqrt(i + 1))) for i in range(D)]) + 1
    return y


def griewank_2d(x, y):
    return 1 / 4000 * (x ** 2 + y ** 2) - np.cos(x / np.sqrt(2)) * np.cos(y / np.sqrt(2)) + 1


def griewank_3d(x, y, z):
    return 1 / 4000 * (x ** 2 + y ** 2 + z ** 2) - np.cos(x / np.sqrt(1)) * np.cos(y / np.sqrt(2)) * np.cos(
        z / np.sqrt(3)) + 1


def michalewicz(x):
    return - np.sin(x) * np.sin(x ** 2 / np.pi) ** 20


def michalewicz_2d(x, y):
    return 2 - (np.sin(x) * np.sin(x ** 2 / np.pi) ** 20) - (np.sin(y) * np.sin(2 * y ** 2 / np.pi) ** 20)


def michalewicz_3d(x, y, z):
    return - (np.sin(x) * np.sin(x ** 2 / np.pi) ** 20) - (np.sin(y) * np.sin(2 * y ** 2 / np.pi) ** 20) - (
            np.sin(z) * np.sin(3 * z ** 2 / np.pi) ** 20)


def rastring(x):
    D = len(x)
    y = 10 * D + np.sum([(x[i] ** 2 - 10 * np.cos(2 * np.pi * x[i])) for i in range(D)])
    return y


def rastring_2d(x, y):
    return 20 + (x ** 2 - 10 * np.cos(2 * np.pi * x)) + (y ** 2 - 10 * np.cos(2 * np.pi * y))


def rastring_3d(x, y, z):
    return 30 + (x ** 2 - 10 * np.cos(2 * np.pi * x)) + (y ** 2 - 10 * np.cos(2 * np.pi * y)) + (
            z ** 2 - 10 * np.cos(2 * np.pi * z))


def rosenbrock_2d(x, y):
    return (x - 1) ** 2 + 10 * (y - x ** 2) ** 2


def rosenbrock_3d(x, y, z):
    return (x - 1) ** 2 + (y - 1) ** 2 + 100 * (- y + x ** 2) ** 2 + 100 * (- z + y ** 2) ** 2


def schwefel(x):
    D = len(x)
    y = (418.9829 * D) - np.sum([x[i] * np.sin(np.sqrt(np.abs(x[i]))) for i in range(D)])
    return y


def schwefel_2d(x, y):
    return 2 * 418.9829 - x * np.sin(np.sqrt(np.abs(x))) - y * np.sin(np.sqrt(np.abs(y)))


def schwefel_3d(x, y, z):
    return 3 * 418.9829 - x * np.sin(np.sqrt(np.abs(x))) - y * np.sin(np.sqrt(np.abs(y))) - z * np.sin(
        np.sqrt(np.abs(z)))


def shubert(x):
    D = len(x)
    y = np.prod([np.sum([i * np.cos(((i + 1) * x[d]) + i for i in range(5))]) for d in range(D)])
    return y


def shubert_2d(x, y):
    res_x = (1 * np.cos(2 * x + 1) + 2 * np.cos(3 * x + 1) + 3 * np.cos(4 * x + 1) + 4 * np.cos(5 * x + 1) + 5 * np.cos(
        6 * x + 1))
    res_y = (1 * np.cos(2 * y + 1) + 2 * np.cos(3 * y + 1) + 3 * np.cos(4 * y + 1) + 4 * np.cos(5 * y + 1) + 5 * np.cos(
        6 * y + 1))
    res = res_x * res_y

    return 200 + res


def shubert_3d(x, y, z):
    res_x = (1 * np.cos(2 * x + 1) + 2 * np.cos(3 * x + 1) + 3 * np.cos(4 * x + 1) + 4 * np.cos(5 * x + 1) + 5 * np.cos(
        6 * x + 1))
    res_y = (1 * np.cos(2 * y + 1) + 2 * np.cos(3 * y + 1) + 3 * np.cos(4 * y + 1) + 4 * np.cos(5 * y + 1) + 5 * np.cos(
        6 * y + 1))
    res_z = (1 * np.cos(2 * z + 1) + 2 * np.cos(3 * z + 1) + 3 * np.cos(4 * z + 1) + 4 * np.cos(5 * z + 1) + 5 * np.cos(
        6 * z + 1))
    res = res_x * res_y * res_z

    return res


def vincent(x):
    D = len(x)
    y = np.sum([np.sin(10 * np.log(x[i])) for i in range(D)])
    return y


def vincent_2d(x, y):
    return np.sin(10 * np.log(x)) + np.sin(10 * np.log(y))


def vincent_3d(x, y, z):
    return np.sin(10 * np.log(x)) + np.sin(10 * np.log(y)) + np.sin(10 * np.log(z))


def xinshe(x):
    D = len(x)
    y = np.sum([(np.abs(x[i]) * (np.exp(np.sum([np.sin(x[k] ** 2) for k in range(D)]))) ** (-1)) for i in range(D)])
    return y


def xinshe_2d(x, y):
    return np.abs(x) * np.abs(np.exp(np.sin(x ** 2) + np.sin(y ** 2))) ** (-1) + np.abs(y) * np.abs(
        np.exp(np.sin(x ** 2) + np.sin(y ** 2))) ** (-1)


def xinshe_3d(x, y, z):
    return np.abs(x) * np.abs(np.exp(np.sin(x ** 2) + np.sin(y ** 2) + np.sin(z ** 2))) ** (-1) \
           + np.abs(y) * np.abs(np.exp(np.sin(x ** 2) + np.sin(y ** 2) + np.sin(z ** 2))) ** (-1) \
           + np.abs(z) * np.abs(np.exp(np.sin(x ** 2) + np.sin(y ** 2) + np.sin(z ** 2))) ** (-1)


def sum_power_2d(x, y):
    res = np.abs(x) ** 2 + np.abs(y) ** 3
    return res


def sum_power_3d(x, y, z):
    res = np.abs(x) ** 2 + np.abs(y) ** 3 + np.abs(z) ** 4
    return res


def g_dec(x, alpha):
    if 0 <= x <= (4 / 5 * alpha):
        res = - (x / alpha) + 4 / 5
    if (4 / 5 * alpha) < x <= alpha:
        res = 5 * x / alpha - 4
    if alpha < x <= (1 + 4 * alpha) / 5:
        res = 5 * (x - alpha) / (alpha - 1) + 1
    if ((1 + 4 * alpha) / 5) < x <= 1:
        res = (x - 1) / (1 - alpha) + 4 / 5

    return res


def deceptive_2d(x, y, alpha_x=0.3, alpha_y=0.7, beta=0.2):
    res = - (1 / 2 * (g_dec(x, alpha_x) + g_dec(y, alpha_y))) ** beta
    return res


def deceptive_3d(x, y, z, alpha_x=0.3, alpha_y=0.7, alpha_z=0.5, beta=0.2):
    res = - (1 / 3 * (g_dec(x, alpha_x) + g_dec(y, alpha_y) + g_dec(z, alpha_z))) ** beta
    return res
