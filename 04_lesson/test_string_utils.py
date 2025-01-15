from string_utils import StringUtils

utils = StringUtils()


def test_capitilize():
    #  Позитивные тесты
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("Skypro") == "Skypro"

    #  Негативные тесты
    assert utils.capitilize("") == ""  # Пустая строка
    assert utils.capitilize(" ") == " "  # Строка с пробелом


def test_trim():
    # Позитивные тесты
    assert utils.trim("  skypro") == "skypro"
    assert utils.trim("  New skypro") == "New skypro"

    # Негативные тесты
    assert utils.trim("") == ""  # Пустая строка


def test_to_list():
    #  Позитивные тесты
    assert utils.to_list('1,2,3') == ['1', '2', '3']
    assert utils.to_list("a,b,c") == ["a", "b", "c"]

    # Негативные тесты
    assert utils.to_list("") == []  # Пустая строка


def test_contains():
    #  Позитивные тесты
    assert utils.contains("skypro", "s") is True
    assert utils.contains("skypro", "d") is False

    #  Негативные тесты
    assert utils.contains("", "s") is False  # Пустая строка


def test_delete_symbol():
    # Позитивные тесты
    assert utils.delete_symbol("skypro", "s") == "kypro"
    assert utils.delete_symbol("skypro", "kypro") == "s"

    #  Негативные тесты
    assert utils.delete_symbol("", "s") == ""  # Пустая строка


def test_starts_with():
    #  Позитивные тесты
    assert utils.starts_with("skypro", "s") is True
    assert utils.starts_with("skypro", "o") is False

    #  Негативные тесты
    assert utils.starts_with("", "s") is False  # Пустая строка


def test_end_with():
    #  Позитивные тесты
    assert utils.end_with("skypro", "o") is True
    assert utils.end_with("skypro", "p") is False

    #  Негативные тесты
    assert utils.end_with("", "o") is False  # Пустая строка


def test_is_empty():
    #  Позитивные тесты
    assert utils.is_empty("") is True

    # Негативные тесты
    assert utils.is_empty("  ") is True  # Строка с пробелами
    assert utils.is_empty("skypro") is False  # строка с названием


def test_list_to_string():
    # Позитивные тесты
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert utils.list_to_string([1,2,3,4]) == "1, 2, 3, 4"

    #  Негативные тесты
    assert utils.list_to_string([]) == ""  # Пустой список
