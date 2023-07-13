import math

from decimal import Decimal
from fastapi import APIRouter

from controllers.centralTendencyMeasurement import tendencia_central
from controllers.dispersionMesurement import dispersion_measure
from controllers.linealRegression import start, get_coeficiente_regresion_l1, get_coeficiente_regresion_l2
from models.Data2 import Data2
from models.Data3 import Data3

from models.data import Data

statistics = APIRouter()


# methods
def set_type_of(data):
    str_data = list(map(str, data))
    if '.' in str(data):
        new_data = list(map(float, str_data))
    else:
        new_data = list(map(int, str_data))
    return new_data


# def get_elements(data):
#     return set_type_of(data.split(','))


def get_decimals_of(data):
    str_data = list(map(str, data))
    max_count = 0
    for x in str_data:
        count = len(x) - x.index('.') - 1
        if count > max_count:
            max_count = count
    return max_count - 1


def set_unit_variable(data):
    if type(data[1]) == float:
        count = get_decimals_of(data)
        return Decimal(f'0.{"0" * count}1')
    else:
        return 1


def get_number_of_clases(size):
    return round((1 + 3.322) * (math.log10(size)))


def get_frecuency(data, number_inf, number_sup):
    count = 0
    for x in data:
        if number_inf <= x <= number_sup:
            count += 1
    return count


def get_statistic_data(data):
    data = sorted(data)
    variable_unit = float(set_unit_variable(data))
    number_of_classes = get_number_of_clases(len(data))
    range = (data[len(data) - 1] - data[0])
    amplitud = int(range / number_of_classes) + 1
    main_data = []

    i = 0
    while i < number_of_classes:
        if i == 0:
            lim_inf = data[0]
        else:
            lim_inf = lim_sup + variable_unit
        lim_sup = (lim_inf + amplitud - float(variable_unit))
        frec = get_frecuency(data, lim_inf, lim_sup)

        main_data.append([i + 1, lim_inf, lim_sup, frec])
        i += 1

    return main_data


@statistics.post("/frecuency-distribution")
def get_frecuency_distribution_table(data: Data):
    original_data = data.data
    data = get_statistic_data(original_data)
    tendencia_central(data)
    return data


@statistics.post("/central-tendency")
def get_central_tendency(data: Data):
    original_data = data.data
    data = get_statistic_data(original_data)
    tendency_data = tendencia_central(data)
    return {
        "media": tendency_data[0],
        "mediana": tendency_data[1],
        "moda": tendency_data[2]
    }


@statistics.post("/dispersion-data")
def get_dispersion(data: Data):
    original_data = data.data
    dispersion_data = dispersion_measure(original_data)
    return {
        "media": dispersion_data[0],
        "varianza": dispersion_data[1],
        "desviacion estandar": dispersion_data[2]}


@statistics.post("/determination-coeficient")
def get_determination_coeficient(data: Data2):
    return round(((start(data.data01, data.data02) ** 2) * 100), 2)


@statistics.post("/relational-coeficient")
def get_relational_coeficient(data: Data2):
    return start(data.data01, data.data02)


@statistics.post("/regretion-coeficient-x")
def get_regretional_coeficient_x(data: Data3):
    return round((get_coeficiente_regresion_l1(data.data01, data.data02, data.number)), 2)


@statistics.post("/regretion-coeficient-y")
def get_regretional_coenficient_y(data: Data3):
    return round((get_coeficiente_regresion_l2(data.data01, data.data02, data.number)), 3)
