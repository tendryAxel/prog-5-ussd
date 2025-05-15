def flatten_dict(dictionary: dict) -> dict:
    return {
        k if not isinstance(v, dict) else k2: v2
        for k, v in dictionary.items()
        for k2, v2 in (
            flatten_dict(v).items() if isinstance(v, dict) else [(k, v)]
        )
    }

def extract_dict(dictionary: dict, content_key_match: str = "content") -> dict:
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
