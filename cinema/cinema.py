class Human:
    def __init__(self, first_name, last_name, patronymic='', place = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.place = place

    def __str__(self):
        if self.patronymic:
            return f'зритель: {self.last_name} {self.first_name[0]} {self.patronymic[0]} место: {self.place}'
        else:
            return f'зритель: {self.last_name} {self.first_name[0]} место: {self.place}.'

    @classmethod
    def import_from_file(cls, file_name):
        items_source = open(file_name, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for items_dict in items_source_as_dict:
            _item = cls(**items_dict)
            items.append(_item)

        return items


class Hall(Human):
    def __init__(self, room_number, film_format, free_spaces):
        self.room_number = room_number
        self.film_format = film_format
        self. free_spaces =  free_spaces


    # def set_group(self, group):
    #     self.group = group

    def __str__(self):
        return f'зал №{self.room_number} формат: {self.film_format}'

    # def __str__(self):
    #     if self.patronymic:
    #         return f'зритель: {self.last_name} {self.first_name[0]}.{self.patronymic[0]}.'
    #     else:
    #         return f'зритель: {self.last_name} {self.first_name[0]}.'




class Cashbox(Human):
    def __init__(self, name_films, price):
        self.name_films = name_films
        self.price = price

    def __str__(self):
        return f'фильм: {self.name_films} цена: {self.price}'

    # def add_students(self, students):
    #     for student in students:
    #         student.set_group(self)

class Pub(Human):
    def __init__(self, eat= '', drink=''):
        self.eat = eat
        self.drink = drink

    # def __str__(self):
    #     if self.patronymic:
    #         return f'учитель ({self.education}): {self.last_name} {self.first_name[0]}.{self.patronymic[0]}.'
    #     else:
    #         return f'учитель ({self.education}): {self.last_name} {self.first_name[0]}.'

    def __str__(self):
        return f'заказ: {self.eat} {self.drink}'