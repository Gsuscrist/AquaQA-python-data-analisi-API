


def tendencia_central(data):
    frec_ac = 0
    frec_co = 0
    unit_variable = 0


    def get_total(data):
        suma = 0
        for z in data:
            suma = suma + z[3]
        return suma


    def set_unit_variable(min_value, sup_value):
        unit_variable = min_value - sup_value
        return unit_variable


    def get_frec_acumulada(frec_ac, frec_ab):
        return frec_ac + frec_ab


    def get_frec_complementaria(total, frec_ab):
        return total - frec_ab


    def get_total(data):
        suma = 0
        for z in data:
            suma = suma + z[3]
        return suma

    def get_class_mark(lim_inf, lim_sup):
        return (lim_inf + lim_sup) / 2


    def complete_data_information(data):
        i = 0
        full_data = []
        for x in data:
            class_mark = get_class_mark(x[1], x[2])
            if i == 0:
                frec_ac = x[3]

                total = get_total(data)
                frec_co = total - x[3]
            else:
                frec_ac = frec_ac + x[3]
                frec_co = get_frec_complementaria(frec_co, x[3])

            i += 1
            x.append(class_mark)
            x.append(frec_ac)
            x.append(frec_co)
            full_data.append(x)
        return full_data

    def get_sup_lim_ex(data):
        full_data = []
        for x in data:
            sup_ex = x[2] + (unit_variable / 2)
            x.append(sup_ex)
            full_data.append(x)
        return full_data


    def get_inf_lim_ex(data):
        full_data = []
        for x in data:
            inf_ex = x[1] - (unit_variable / 2)
            x.append(inf_ex)
            full_data.append(x)
        return full_data


    def get_media(data):
        media_base = 0
        for x in data:
            media_base = media_base + x[3] * x[4]
        total = get_total(data)
        media = media_base / total
        return media


    def get_pm(data):
        total = get_total(data)
        pm = (total + 1) / 2
        return pm


    def get_mediana_class(number):
        counter = 0
        for x in data:
            if x[5] < number:
                counter += 1
        return counter


    def get_ancho_intervalo(data):
        array = data[0]
        ancho = (array[8] - array[7])
        return ancho


    def get_mediana(data, class_number):
        array = data[class_number]

        try:
            frec_ant = data[class_number - 1][5]
        except IndexError:
            frec_ant = 0
        else:
            frec_ant = data[class_number - 1][5]

        mediana = array[7] + ((((get_total(data) / 2) - frec_ant) / array[3]) * get_ancho_intervalo(data))
        return mediana


    def get_modal_class(data):
        modal_class = data.index(max(data, key=lambda x: x[3]))
        return modal_class


    def get_moda(data, number):
        moda_class = data[number]
        # poner variables de valor class_ant y class_anterior y si no existen poner 0

        try:
            frec_class_ant = data[number - 1][3]
        except IndexError:
            frec_class_ant = 0
        else:
            frec_class_ant = data[number - 1][3]
        try:
            frec_class_sig = data[number + 1][3]
        except IndexError:
            frec_class_sig = 0
        else:
            frec_class_sig = data[number + 1][3]
        moda = moda_class[7] + (((moda_class[3] - data[number - 1][3]) / (
                (2 * moda_class[3]) - frec_class_ant - frec_class_sig)) * get_ancho_intervalo(data))
        return moda

    def mediana(data):
        mediana_position = get_pm(data)
        mediana_clase = get_mediana_class(mediana_position)
        mediana = get_mediana(data, mediana_clase)
        return mediana

    def moda(data):
        moda_clase = get_modal_class(data)
        moda = get_moda(data, moda_clase)
        return moda

    ############
    complete_data_information(data)
    unit_variable = set_unit_variable(data[1][1], data[0][2])
    data = get_inf_lim_ex(data)
    data = get_sup_lim_ex(data)

    # logica del tema
    media = get_media(data)
    mediana = mediana(data)
    moda = moda(data)

    return [media, mediana, moda]
