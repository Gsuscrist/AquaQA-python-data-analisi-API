import math


def dispersion_measure(data):
    def get_media(data):
        media = 0
        for i in data:
            media += i
        media = media / len(data)
        return media

    def get_varianza(data, media):
        varianza = 0
        for x in data:
            varianza += ((x - media) ** 2)

        return varianza / len(data)

    def get_desviacion(varianza):
        return math.sqrt(varianza)

    data = sorted(data)
    media = get_media(data)
    varianza = get_varianza(data, media)
    de = get_desviacion(varianza)

    return [media, varianza, de]
