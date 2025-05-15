import doctest


class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float) -> None:
        """
        Создание и подготовка к работе объекта "Стакан".

        :param capacity_volume: Объем стакана (должен быть положительным числом)
        :param occupied_volume: Объем занимаемой жидкости (неотрицательное число)

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.capacity_volume
        500.0
        >>> glass.occupied_volume
        0.0
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = float(capacity_volume)

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть типа int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        if occupied_volume > capacity_volume:
            raise ValueError(
                "Начальное количество жидкости не может превышать вместимость стакана"
            )
        self.occupied_volume = float(occupied_volume)

    def is_empty_glass(self) -> bool:
        """
        Проверяет, пуст ли стакан.

        :return: True, если в стакане нет жидкости, иначе False

        Примеры:
        >>> Glass(500, 0).is_empty_glass()
        True
        >>> Glass(500, 100).is_empty_glass()
        False
        """
        return self.occupied_volume == 0.0

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавляет воду в стакан.

        :param water: Объем добавляемой жидкости (положительное число)
        :raise TypeError: если water не int или float
        :raise ValueError: если water отрицательно или превышает свободный объём

        Примеры:
        >>> g = Glass(500, 100)
        >>> g.add_water_to_glass(50)
        >>> g.occupied_volume
        150.0
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        water = float(water)
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")

        free_space = self.capacity_volume - self.occupied_volume
        if water > free_space:
            raise ValueError(f"Добавляемая вода ({water}) превышает свободный объём ({free_space})")
        self.occupied_volume += water

    def remove_water_from_glass(self, estimate_water: float) -> float:
        """
        Убирает воду из стакана.

        :param estimate_water: Объём извлекаемой жидкости (положительное число)
        :raise TypeError: если estimate_water не int или float
        :raise ValueError: если estimate_water отрицательно или превышает текущий объём
        :return: Объём реально извлечённой жидкости

        Примеры:
        >>> g = Glass(500, 300)
        >>> removed = g.remove_water_from_glass(100)
        >>> removed
        100.0
        >>> g.occupied_volume
        200.0
        """
        if not isinstance(estimate_water, (int, float)):
            raise TypeError("Извлекаемая жидкость должна быть типа int или float")
        estimate_water = float(estimate_water)
        if estimate_water < 0:
            raise ValueError("Извлекаемая жидкость должна быть положительным числом")

        if estimate_water > self.occupied_volume:
            raise ValueError(
                f"Запрашиваемый объём ({estimate_water}) превышает текущее количество ({self.occupied_volume})"
            )
        self.occupied_volume -= estimate_water
        return estimate_water


class Cup:
    def __init__(self, diameter: float, height: float) -> None:
        """
        Инициализация объекта 'Чашка'.

        :param diameter: Диаметр чашки
        :param height: Высота чашки
        """
        if not isinstance(diameter, (int, float)):
            raise TypeError("Диаметр должен быть числом")
        if diameter <= 0:
            raise ValueError("Диаметр должен быть положительным числом")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть числом")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.diameter = float(diameter)
        self.height = float(height)

    def volume(self) -> float:
        """
        Вычисляет приблизительный объем чашки (цилиндрическая форма).

        :return: Объем чашки
        """
        from math import pi
        radius = self.diameter / 2
        return pi * radius * radius * self.height

    def describe(self) -> str:
        """
        Возвращает строковое описание чашки.

        :return: Описание чашки
        """
        return f"Чашка: диаметр={self.diameter}, высота={self.height}"


class Bottle:
    def __init__(self, volume_ml: int, brand: str) -> None:
        """
        Инициализация объекта 'Бутылка'.

        :param volume_ml: Объем бутылки в миллилитрах
        :param brand: Бренд бутылки
        """
        if not isinstance(volume_ml, int):
            raise TypeError("Объем бутылки должен быть целым числом")
        if volume_ml <= 0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not brand:
            raise ValueError("Бренд не может быть пустым")
        self.volume_ml = volume_ml
        self.brand = brand

    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли бутылка (нет жидкости).

        :return: True, если бутылка пуста
        """
        return self.volume_ml == 0

    def fill(self, amount_ml: int) -> None:
        """
        Добавляет воду в бутылку.

        :param amount_ml: Объем добавляемой жидкости
        :raise TypeError: если amount_ml не int
        :raise ValueError: если amount_ml отрицательно
        """
        if not isinstance(amount_ml, int):
            raise TypeError("Количество должно быть целым числом")
        if amount_ml < 0:
            raise ValueError("Количество должно быть неотрицательным")
        self.volume_ml += amount_ml

    def empty(self, amount_ml: int) -> int:
        """
        Убирает воду из бутылки.

        :param amount_ml: Объем удаляемой жидкости
        :return: Фактически удаленный объем
        :raise TypeError: если amount_ml не int
        :raise ValueError: если amount_ml отрицательно или превышает текущий объем
        """
        if not isinstance(amount_ml, int):
            raise TypeError("Количество должно быть целым числом")
        if amount_ml < 0:
            raise ValueError("Количество должно быть неотрицательным")
        if amount_ml > self.volume_ml:
            raise ValueError("Запрашиваемый объем превышает текущий объем")
        self.volume_ml -= amount_ml
        return amount_ml


if __name__ == "__main__":
    doctest.testmod()
