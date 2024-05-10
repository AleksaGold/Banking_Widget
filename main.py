import operator

from src.utils import load_operations, reformat_the_date, disguise_number


def main():
    """
    Запускает основной код
    :return:
    """
    executed_operations = [operation for operation in load_operations() if operation.get('state') == 'EXECUTED']

    sorted_operations = sorted(executed_operations, key=operator.itemgetter('date'), reverse=True)

    operations_new_date_format = reformat_the_date(sorted_operations)

    operations_disguise_number_to = disguise_number(operations_new_date_format, 'from')
    operations_disguise_number_from = disguise_number(operations_disguise_number_to, 'to')

    for operation in operations_disguise_number_from[:5]:
        print(f"{operation['date']} {operation['description']}\n"
              f"{operation['from']}-> {operation['to']}\n"
              f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")


if __name__ == '__main__':
    main()
