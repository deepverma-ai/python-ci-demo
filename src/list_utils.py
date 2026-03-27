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


def filter_and_transform(items: list, threshold: int) -> list:
    """A more complex function to drop coverage further."""
    if not isinstance(items, list):
        return []

    result: list = []
    for x in items:
        if isinstance(x, (int, float)):
            if x > threshold:
                result.append(x * 10)
            else:
                result.append(x / 10)
        else:
            result.append(str(x))
    return result
