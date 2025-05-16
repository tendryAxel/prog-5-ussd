from functools import reduce


def flatten_dict(dictionary: dict) -> dict:
    return {
        k if not isinstance(v, dict) else k2: v2
        for k, v in dictionary.items()
        for k2, v2 in (
            flatten_dict(v).items() if isinstance(v, dict) else [(k, v)]
        )
    }

def _extract_dict(dictionary: dict, content_key_match: str = "content") -> dict:
    return {
        k if not (isinstance(v, dict) and content_key_match in v) else sub_k: sub_v
        for k, v in dictionary.items()
        for sub_k, sub_v in (
            dict(
                [(k, v[content_key_match])] + [(sk, sv) for sk, sv in v.items() if sk != content_key_match]
            ).items()
            if isinstance(v, dict) and content_key_match in v else [(k, v)]
        )
    }

def extract_dict(dictionary: dict, content_key_match: str = "content") -> dict:
    return reduce(
        lambda tmp_dictionary, _: _extract_dict(tmp_dictionary, content_key_match),
        range(max_depth_dict(dictionary)),
        dictionary
    )

def max_depth_dict(dictionary: dict) -> int:
    return 0 \
        if (not isinstance(dictionary, dict) or not dictionary) \
        else 1 + max(max_depth_dict(v) for v in dictionary.values())
