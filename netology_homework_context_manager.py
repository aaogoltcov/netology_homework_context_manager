from datetime import datetime
from contextlib import contextmanager
from pprint import pprint, pformat

''' ЗАДАЧА 1, ВАРИАНТ 1 '''

print('Задача 1 (вариант 1, классы):')


class time_delta:
    @staticmethod
    def time_start():
        start_time = datetime.today()
        print(f'Время старта класса Open: {start_time}')
        return start_time

    @staticmethod
    def time_end(start_time):
        end_time = datetime.today()
        print(f'Время завершения класса Open: {end_time}')

        start_time_seconds = datetime.timestamp(start_time)
        end_time_seconds = datetime.timestamp(end_time)
        delta_of_time = end_time_seconds - start_time_seconds
        if delta_of_time < 1:
            delta_of_time = delta_of_time * 1000000
            print(f'Общее время работы класса Open: {round(delta_of_time)} микросекунд')
        else:
            print(f"Общее время работы класса Open: {round(delta_of_time)} секунд")


class ClassOpen(object):

    def __init__(self, path, flag):
        self.path = path
        self.flag = flag

    def __enter__(self):
        global start_time
        start_time = time_delta.time_start()
        try:
            self.file = open(self.path)
        except IOError:
            self.file = open(self.path, "w")
        return self.file

    def __exit__(self, exp_type, exp_value, exp_tr):
        """ подавляем все исключения IOError """
        if exp_type is IOError:
            self.file.close()  # закрываем файл
            return True
        self.file.close()  # закрываем файл
        time_delta.time_end(start_time)


with ClassOpen("recipes.txt", "r") as file:
    lines = list(line.split(" | ") for line in (lines.strip() for lines in file) if line)
    # print(lines)

''' ЗАДАЧА 1, ВАРИАНТ 2 '''

print('\nЗадача 1 (вариант 2, контекстный менеджер):')


@contextmanager
def ContextOpen(file_path):
    try:
        time_delta.time_start()
        file_object = open(file_path)
        yield file_object
    finally:
        file_object.close()
        time_delta.time_end(start_time)


with ContextOpen('recipes.txt') as file:
    lines = list(line.split(" | ") for line in (lines.strip() for lines in file) if line)
    # print(lines)

''' ЗАДАЧА 2, ВАРИАНТ 1 '''

print('\nЗадача 2 (вариант 1, классы):')
with ClassOpen('recipes.txt', 'r') as file:
    lines = list(line.split(" | ") for line in (lines.strip() for lines in file) if line)


    def main():  # Основная функция

        current_line_count = int()  # Текущий номер цикла
        reciept = str()  # Рецепт
        previous_line_length = int()  # Длина списка предыдущего цикла
        cook_book = {}  # Книга рецептов
        cook_book_line = {}  # Рецепт блюда в книге рецептов
        ingredients_amount = int()  # Количество ингредиентов

        # print('Список рецептов из файла: ')
        for line in lines:
            ingredient = {}  # Список ингридентов
            if len(line) == 1 and (previous_line_length == 0 or previous_line_length > 1):
                reciept = dish_define(cook_book_line, cook_book, reciept, current_line_count)
            elif len(line) == 1 and previous_line_length == 1:
                ingredients_amount = ingredient_count(ingredients_amount, current_line_count)
            elif 1 < len(line) <= ingredients_amount:
                ingredients_list(ingredient, line, reciept, cook_book, cook_book_line)
            previous_line_length = len(line)
            current_line_count += 1
        # pprint(cook_book, width=100)
        # print()


    # Функция выбора блюда
    def dish_define(cook_book_line, cook_book, reciept, current_line_count):
        reciept = ''.join(map(str, lines[current_line_count]))
        cook_book_line.update({reciept: []})
        cook_book.update(cook_book_line)
        return reciept


    #  Функция определения количества ингридентов
    def ingredient_count(ingredients_amount, current_line_count):
        count = ''.join(map(str, lines[current_line_count]))
        ingredients_amount = int(count)
        return ingredients_amount


    # Функция определения ингридиентов для блюда
    def ingredients_list(ingredient, line, reciept, cook_book, cook_book_line):
        ingredient_line = {'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]}
        ingredient.update(ingredient_line)
        for key, value in cook_book.items():
            if key == reciept:
                value.append(ingredient)
                cook_book_line.update({reciept: value})
                cook_book.update(cook_book_line)


    main()

''' ЗАДАЧА 2, ВАРИАНТ 2 '''

print('\nЗадача 2 (вариант 2, контекстный менеджер):')
with ContextOpen('recipes.txt') as file:
    lines = list(line.split(" | ") for line in (lines.strip() for lines in file) if line)


    def main():  # Основная функция

        current_line_count = int()  # Текущий номер цикла
        reciept = str()  # Рецепт
        previous_line_length = int()  # Длина списка предыдущего цикла
        cook_book = {}  # Книга рецептов
        cook_book_line = {}  # Рецепт блюда в книге рецептов
        ingredients_amount = int()  # Количество ингредиентов

        # print('Список рецептов из файла: ')
        for line in lines:
            ingredient = {}  # Список ингридентов
            if len(line) == 1 and (previous_line_length == 0 or previous_line_length > 1):
                reciept = dish_define(cook_book_line, cook_book, reciept, current_line_count)
            elif len(line) == 1 and previous_line_length == 1:
                ingredients_amount = ingredient_count(ingredients_amount, current_line_count)
            elif 1 < len(line) <= ingredients_amount:
                ingredients_list(ingredient, line, reciept, cook_book, cook_book_line)
            previous_line_length = len(line)
            current_line_count += 1
        # pprint(cook_book, width=100)
        # print()


    # Функция выбора блюда
    def dish_define(cook_book_line, cook_book, reciept, current_line_count):
        reciept = ''.join(map(str, lines[current_line_count]))
        cook_book_line.update({reciept: []})
        cook_book.update(cook_book_line)
        return reciept


    #  Функция определения количества ингридентов
    def ingredient_count(ingredients_amount, current_line_count):
        count = ''.join(map(str, lines[current_line_count]))
        ingredients_amount = int(count)
        return ingredients_amount


    # Функция определения ингридиентов для блюда
    def ingredients_list(ingredient, line, reciept, cook_book, cook_book_line):
        ingredient_line = {'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]}
        ingredient.update(ingredient_line)
        for key, value in cook_book.items():
            if key == reciept:
                value.append(ingredient)
                cook_book_line.update({reciept: value})
                cook_book.update(cook_book_line)


    main()
