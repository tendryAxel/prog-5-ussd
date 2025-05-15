import pytest

from src.utils import flatten_dict


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
