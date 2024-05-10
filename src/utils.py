import json
from settings import OPERATIONS_PATH
import datetime


def load_operations():
    """
    Загружает список операций из файла формата json
    :return: список операций
    """
    with open(OPERATIONS_PATH, 'r') as file:
        return json.load(file)


def reformat_the_date(operations: list):
    """
    Переводит дату совершения операций в формат ДД.ММ.ГГГГ
    :param operations: список операций
    :return: список операций с датой в формате ДД.ММ.ГГГГ
    """
    for old_date_format in operations:
        new_date_format = datetime.datetime.fromisoformat(old_date_format['date']).strftime('%d.%m.%Y')
        old_date_format['date'] = new_date_format
    return operations


def disguise_number(operations: list, key='word'):
    """
    Маскирует номер карты и(или) счета
    :param operations: список операций
    :param key: ключ для поиска номера карты и (или) счета с которого/на который переводились деньги
    :return: список операций с замаскированными номерами карты и(или) счета
    """
    for operation in operations:
        if operation.get(key) is None:
            operation[key] = ''
        elif 'Счет' in operation.get(key):
            operation[key] = 'Счет **'+operation[key][-4:]+' '
        else:
            card_name = operation[key].split(' ')
            card_name[-1] = card_name[-1][0:4] + ' '+card_name[-1][4:6]+'** **** '+card_name[-1][12:]+' '
            operation[key] = ' '.join(card_name)
    return operations
