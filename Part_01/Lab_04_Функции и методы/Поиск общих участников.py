def find_common_participants(group1: str, group2: str, delimiter: str = ',') -> list[str]:

    set1 = set(group1.split(delimiter))
    set2 = set(group2.split(delimiter))


    common = sorted(set1 & set2)
    return common


if __name__ == "__main__":

    participants_first_group = "Иванов|Петров|Сидоров"
    participants_second_group = "Петров|Сидоров|Смирнов"

    result_pipe = find_common_participants(participants_first_group,
                                           participants_second_group,
                                           delimiter='|')
    print("Общие участники (|):", result_pipe)


    g1 = "Anna,Bob,Charlie"
    g2 = "Bob,Dave,Charlie"
    result_comma = find_common_participants(g1, g2)
    print("Общие участники (,):", result_comma)