from enum import Enum


class FilterEnum(str, Enum):
    SCREEN_SIZE = "Размер экрана"
    IN_COMPARISON = "В сравнении"

    def __str__(self):
        return self.value


