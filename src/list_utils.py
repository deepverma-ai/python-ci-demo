def remove_duplicates(items: list) -> list:
    if not isinstance(items, list):
        raise TypeError("Input must be a list")
    return list(dict.fromkeys(items))


def find_max(items: list) -> int:
    if not items:
        raise ValueError("List cannot be empty")
    return max(items)


def flatten_list(nested_list: list) -> list:
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")

    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(item)
        else:
            flat.append(item)
    return flat


def count_occurrences(items: list, value) -> int:
    return items.count(value)


def find_min(items: list) -> int:
    if not items:
        raise ValueError("List cannot be empty")
    return min(items)
