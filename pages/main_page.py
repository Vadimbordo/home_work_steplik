from .base_page import BasePage


class MainPage(BasePage):
    """
    https://stepik.org/lesson/201964/step/8?unit=176022

    В классе MainPage у нас не осталось никаких методов, поэтому добавим туда заглушку:
    Как вы уже знаете, метод __init__ вызывается при создании объекта.
    Конструктор выше с ключевым словом super на самом деле только вызывает конструктор
    класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage.
    По сути, такая конструкция нужна для совместимости с python 2
    В python 3 можно заменить на pass

    """
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

