import pytest

from src.utils import flatten_dict, extract_dict


@pytest.mark.parametrize("input_dict, expected", [
    # Cas simple : dictionnaire plat
    (
        {'a': 1, 'b': 2},
        {'a': 1, 'b': 2}
    ),

    # Dictionnaire vide
    (
        {},
        {}
    ),

    # Une seule imbrication
    (
        {'a': {'b': 1}},
        {'b': 1}
    ),

    # Plusieurs niveaux d'imbrication
    (
        {'x': {'y': {'z': 42}}, 'a': 1},
        {'z': 42, 'a': 1}
    ),

    # Clés imbriquées différentes
    (
        {
            'data': {
                'name': 'Alice',
                'details': {
                    'age': 30,
                    'city': 'Paris'
                }
            },
            'status': 'active'
        },
        {
            'name': 'Alice',
            'age': 30,
            'city': 'Paris',
            'status': 'active'
        }
    ),

    # Collisions de clés : les dernières gagnent
    (
        {
            'level1': {
                'value': 100
            },
            'level2': {
                'value': 200
            }
        },
        {
            'value': 200  # écrase la précédente
        }
    ),

    # Mélange de profondeur et de valeurs simples
    (
        {
            'a': {
                'b': {
                    'c': 1
                }
            },
            'd': 2,
            'e': {
                'f': 3
            }
        },
        {
            'c': 1,
            'd': 2,
            'f': 3
        }
    )
])
def test_aplatir_dictionary_cle(input_dict, expected):
    assert flatten_dict(input_dict) == expected

@pytest.mark.parametrize("input_dict, expected", [
    # Cas simple sans dictionnaires
    (
        {"a": 1, "b": 2},
        {"a": 1, "b": 2}
    ),

    # Dictionnaire avec "content"
    (
        {"a": "b", "d": {"content": "e", "f": "g"}},
        {"a": "b", "d": "e", "f": "g"}
    ),

    # Dictionnaire avec "content" uniquement
    (
        {"d": {"content": "e"}},
        {"d": "e"}
    ),

    # Dictionnaire sans "content"
    (
        {"d": {"x": "y"}},
        {"d": {"x": "y"}}
    ),

    # Plusieurs clés avec content
    (
        {
            "a": "A",
            "b": {
                "content": "B",
                "extra": "E"
            },
            "c": {
                "content": "C"
            }
        },
        {
            "a": "A",
            "b": "B",
            "extra": "E",
            "c": "C"
        }
    ),

    # Clé simple + promotion de clé conflictuelle
    (
        {
            "conflict": "outside",
            "x": {
                "content": "inside",
                "conflict": "shadow"
            }
        },
        {
            "conflict": "shadow",  # "shadow" écrase "outside"
            "x": "inside"
        }
    ),

    # Dictionnaire vide
    (
        {},
        {}
    ),

    # peut gerer les sub content
    (
            {
                "conflict": "outside",
                "x": {
                    "content": "inside",
                    "conflict": {
                        "content": "shadow",
                    }
                }
            },
            {
                "conflict": "shadow",
                "x": "inside"
            }
    ),
])
def test_extract_dictionary(input_dict, expected):
    assert extract_dict(extract_dict(input_dict)) == expected

