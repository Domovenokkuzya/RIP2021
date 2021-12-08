from operator import itemgetter


class Producer:
    """Производитель"""

    def __init__(self, id, name, revenue, DET_id):
        self.id = id
        self.name = name
        self.revenue = revenue
        """выручка в млн. руб., информация берётся из интернета"""
        self.DET_id = DET_id
        """Одна из производимых деталей"""


class Detail:
    """Детали"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class ProducerDET:
    """Производители по деталям"""

    def __init__(self, DET_id, PROD_id):
        self.DET_id = DET_id
        self.PROD_id = PROD_id


# Детали
DETs = [
    Detail(1, 'Shaft'),
    Detail(2, 'Key'),
    Detail(3, 'Sheave)'),
    Detail(4, 'Sprocket'),
    Detail(5, 'Gear'),
    Detail(6, 'Nut'),
    Detail(7, 'Crankshaft')
]

# Производители
PRODs = [
    Producer(1, 'Metmash', 428, 1),
    Producer(2, 'Sarzni', 8, 6),
    Producer(3, 'Szinw', 260, 2),
    Producer(4, 'Avtodetal', 3084, 1),
    Producer(5, 'Ogmeh', 95, 4),
    Producer(6, 'Millevorselmash', 140, 3),
    Producer(7, 'Chelzto', 20, 3),
    Producer(8, 'Mehz', 425, 6),
    Producer(9, 'Omzavod', 1037, 7),
    Producer(10, 'Demz', 180, 3),
    Producer(11, 'KZM', 40, 5),
    Producer(12, 'Chzm', 127, 2)
]

# Производители по деталям
PROD_in_DET = [
    ProducerDET(1, 1),
    ProducerDET(1, 4),
    ProducerDET(2, 3),
    ProducerDET(2, 12),
    ProducerDET(3, 6),
    ProducerDET(3, 7),
    ProducerDET(3, 10),
    ProducerDET(4, 5),
    ProducerDET(5, 11),
    ProducerDET(6, 2),
    ProducerDET(6, 8),
    ProducerDET(7, 9),

    ProducerDET(1, 12),
    ProducerDET(2, 6),
    ProducerDET(3, 9),
    ProducerDET(4, 1),
    ProducerDET(5, 12),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(prod.name, prod.revenue, det.name)
                   for prod in PRODs
                   for det in DETs
                   if prod.DET_id == det.id]

    print('\n\n\n\nЗадание А1')
    # сортировка по возрастанию выручки производителей
    print(sorted(one_to_many, key=itemgetter(1)))

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(det.name, proddet.DET_id, proddet.PROD_id)
                         for det in DETs
                         for proddet in PROD_in_DET
                         if det.id == proddet.DET_id]

    print('\nЗадание А2')
    # Т.к. была взята выручка, то сменил на среднюю выручку
    res_12_unsorted = []
    # Считаем среднюю выручку производителей
    for det in DETs:
        # Сумма выручек производителей
        DET_sum = sum(prod.revenue for prod in PRODs if (det.id == prod.DET_id))
        # Количество производитлей для детали
        DET_numer_of_prods = len(list(filter(lambda i: i[2] == det.name, one_to_many)))
        # Средняя выручка производителей, занимающихся производтсвом этой детали
        DET_average = DET_sum / DET_numer_of_prods
        res_12_unsorted.append((det.name, DET_average))
    # Сортировка по выручке
    print(sorted(res_12_unsorted, key=itemgetter(1)))

    many_to_many = [(prod.name, prod.revenue, DET_name)
                    for DET_name, DET_id, prod_id in many_to_many_temp
                    for prod in PRODs
                    if prod.id == prod_id]

    print('\nЗадание А3')
    # вывод Производителей для деталей, названия которых длиннее 5 букв
    res_13 = {}
    for det in DETs:
        if len(det.name) > 5:
            # Список деталей
            det_in_prod = list(filter(lambda i: i[2] == det.name, many_to_many))
            # Оставляем только названия
            prod_in_det_names = [name for name, _, _ in det_in_prod]
            # Добавляем результат в словарь
            # ключ - деталь, значение - список производителей
            res_13[det.name] = prod_in_det_names
    print(res_13)


if __name__ == '__main__':
    main()