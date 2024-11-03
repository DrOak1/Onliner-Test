from enum import Enum


class ComparePageEnum(str, Enum):
    OS = "Операционная система"
    SCREEN_SIZE = "Размер экрана"
    SCREEN_DIMENSION = "Разрешение экрана"
    RAM = "Объем оперативной памяти"
    MEMORY = "Объем встроенной памяти"

    def __str__(self):
        return self.value
