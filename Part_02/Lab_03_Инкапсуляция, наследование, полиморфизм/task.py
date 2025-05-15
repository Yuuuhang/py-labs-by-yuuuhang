class Book:
    def __init__(self, name: str, author: str) -> None:
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int) -> None:
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("pages must be int")
        if value <= 0:
            raise ValueError("pages must be > 0")
        self._pages = value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(name={self.name!r}, "
            f"author={self.author!r}, pages={self.pages})"
        )


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float) -> None:
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise TypeError("duration must be float‑compatible")
        if value <= 0:
            raise ValueError("duration must be > 0")
        self._duration = value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(name={self.name!r}, "
            f"author={self.author!r}, duration={self.duration})"
        )
