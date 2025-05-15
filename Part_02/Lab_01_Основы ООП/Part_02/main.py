from task_1 import Glass, Bottle, Cup


def main() -> None:
    # 1. корректные объекты (создаются без ошибок)
    glass = Glass(500, 100)          # 500 мл, 100 мл занято
    bottle = Bottle(750, "Evian")    # 750 мл, бренд Evian
    cup = Cup(8.0, 10.0)             # диаметр 8 см, высота 10 см

    # 2. намеренно неверные вызовы — ДОЛЖНЫ выбрасывать TypeError/ValueError
    tests = [
        (glass.add_water_to_glass, ("a lot",)),  # str вместо числа  → TypeError
        (bottle.fill,            (-50,)),        # отрицательное     → ValueError
        (bottle.empty,           ("many",)),     # str вместо int    → TypeError
    ]

    for func, args in tests:
        try:
            func(*args)
        except (TypeError, ValueError):
            print("Ошибка: неправильные данные")


if __name__ == "__main__":
    main()
