def flatten_dict(dictionary: dict) -> dict:
    return {
        k if not isinstance(v, dict) else k2: v2
        for k, v in dictionary.items()
        for k2, v2 in (
            flatten_dict(v).items() if isinstance(v, dict) else [(k, v)]
        )
    }
