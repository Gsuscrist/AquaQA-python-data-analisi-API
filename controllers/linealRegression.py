import math


def organice_data(l1, l2):
    data = [];
    max_length = max(len(l1), len(l2))
    for i in range(max_length):
        x = l1[i] if i < len(l1) else 0
        y = l2[i] if i < len(l2) else 0
        data.append([x, y])

    return data


def get_media(list):
    count = 0
    for x in list:
        count += x
    return count / len(list)


def fill_data(data, l1_media, l2_media):
    new_data = []
    for x in data:
        l1 = x[0]
        l2 = x[1]
        dif1 = round((l1 - l1_media) ** 2, 3)
        dif2 = round((l2 - l2_media) ** 2, 3)
        multidifs = round((l1 - l1_media) * (l2 - l2_media), 3)
        new_data.append([l1, l2, dif1, dif2, multidifs])
    return new_data


def get_covarianza(data):
    count = 0
    for x in data:
        count += x[4]
    return round(count / len(data), 3)


def get_de(data, position):
    count = 0
    for x in data:
        count += x[position]
    count = count / len(data)
    return round(math.sqrt(count), 3)


def get_coeficiente_correlacion_lineal_pearson(l1, l2):
    data = organice_data(l1, l2)
    l1_media = get_media(l1)
    l2_media = get_media(l2)
    data = fill_data(data, l1_media, l2_media)
    covarianza = get_covarianza(data)
    del1 = get_de(data, 2)
    del2 = get_de(data, 3)
    return round((covarianza / (del1 * del2)), 3)


def get_l1b(covarianza, del1):
    return round((covarianza / (del1 ** 2)), 3)


def get_l1a(l1_media, l2_media, b):
    return round((l2_media - (b * l1_media)), 3)


def get_coeficiente_regresion_l1(l1, l2, number):
    data = organice_data(l1, l2)
    l1_media = get_media(l1)
    l2_media = get_media(l2)
    data = fill_data(data, l1_media, l2_media)
    covarianza = get_covarianza(data)
    del1 = get_de(data, 2)
    print("1 ", get_l1a(l1_media, l2_media, get_l1b(covarianza, del1)))
    print("2 ", (get_l1b(covarianza, del1) * number))
    return get_l1a(l1_media, l2_media, get_l1b(covarianza, del1)) + (get_l1b(covarianza, del1) * number)


def get_l2a(l1_media, l2_media, b):
    return l1_media - (b * l2_media)


def get_coeficiente_regresion_l2(l1, l2, number):
    data = organice_data(l1, l2)
    l1_media = get_media(l1)
    l2_media = get_media(l2)
    data = fill_data(data, l1_media, l2_media)
    covarianza = get_covarianza(data)
    del2 = get_de(data, 3)
    return get_l2a(l1_media, l2_media, covarianza / (del2 ** 2)) + (covarianza / (del2 ** 2) * number)


def start(l1, l2):
    return get_coeficiente_correlacion_lineal_pearson(l1, l2)

def get_points(data1, data2):
    max_length = max(len(data1), len(data2))
    data1 += [0.0] * (max_length - len(data1))
    data2 += [0.0] * (max_length - len(data2))
    tuplas_combinadas = zip(data1,data2)
    tuplas_con_tres_decimales = [(round(a, 3), round(b, 3)) for a, b in tuplas_combinadas]
    lista_combinada = [list(tupla) for tupla in tuplas_con_tres_decimales]

    return lista_combinada
