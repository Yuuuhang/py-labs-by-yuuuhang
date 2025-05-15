"""
Лабораторная работа 4 / Задание 1
Файл: task.py
Описание:
    Демонстрация базового и дочернего классов с наследованием,
    перегрузкой методов и инкапсуляцией.

Python 3.11+
"""

from __future__ import annotations

class Vehicle:
    """
    Базовый класс «Транспортное средство».

    Причина инкапсуляции:
        - _engine_running защищён: запрещаем прямой доступ извне,
          чтобы сохранить целостность состояния двигателя.
    """

    def __init__(self,
                 brand: str,
                 model: str,
                 year: int,
                 max_speed: float) -> None:
        """
        Параметры
        ----------
        brand : str
            Производитель.
        model : str
            Модель.
        year : int
            Год выпуска.
        max_speed : float
            Конструктивная максимальная скорость (км/ч).
        """
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self.max_speed: float = max_speed

        self._engine_running: bool = False      # защищённый атрибут
        self._speed: float = 0.0                # текущая скорость

    # --------------- Магические методы ---------------

    def __str__(self) -> str:
        return (f"{self.brand} {self.model} ({self.year}) — "
                f"{self._speed:.0f}/{self.max_speed} км/ч")

    def __repr__(self) -> str:  # pragma: no cover
        return (f"{self.__class__.__name__}("
                f"brand={self.brand!r}, model={self.model!r}, "
                f"year={self.year!r}, max_speed={self.max_speed!r})")

    # --------------- Публичные методы ---------------

    def start_engine(self) -> None:
        """Запускает двигатель."""
        self._engine_running = True

    def stop_engine(self) -> None:
        """Глушит двигатель и сбрасывает скорость до 0."""
        self._engine_running = False
        self._speed = 0.0

    def accelerate(self, delta: float) -> None:
        """
        Увеличивает скорость.

        Параметры
        ----------
        delta : float
            Приращение скорости (км/ч).
        """
        if not self._engine_running:
            raise RuntimeError("Двигатель не запущен")
        self._speed = min(self._speed + delta, self.max_speed)

    def brake(self, delta: float) -> None:
        """
        Замедляет движение.

        Параметры
        ----------
        delta : float
            Значение снижения скорости (км/ч).
        """
        self._speed = max(self._speed - delta, 0.0)

    # --------------- Геттеры ---------------

    @property
    def speed(self) -> float:
        """Текущая скорость (км/ч)."""
        return self._speed


class PassengerCar(Vehicle):
    """
    Дочерний класс «Легковой автомобиль».

    Перегружает метод `accelerate`, добавляя проверку
    количества пассажирских мест; это демонстрирует
    специализацию поведения для конкретного вида ТС.
    """

    def __init__(self,
                 brand: str,
                 model: str,
                 year: int,
                 max_speed: float,
                 seats: int = 5) -> None:
        """
        Расширяет конструктор базового класса новым атрибутом.

        Параметры
        ----------
        seats : int
            Количество посадочных мест.
        """
        super().__init__(brand, model, year, max_speed)
        self.seats: int = seats

    # ---------- Перегрузка магического метода ----------

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | мест: {self.seats}"

    # ---------- Перегрузка обычного метода -------------

    def accelerate(self, delta: float) -> None:
        """
        Ускорение с учётом загруженности салона.

        Причина перегрузки
        ------------------
        У легкового авто максимальное ускорение
        зависит от количества пассажирских мест:
        чем их больше — тем выше масса, следовательно,
        ниже возможное приращение скорости.
        """
        load_factor = 1.0 + (self.seats - 1) * 0.02  # простая модель
        adjusted_delta = delta / load_factor
        super().accelerate(adjusted_delta)
