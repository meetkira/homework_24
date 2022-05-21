import re
from typing import Any, Iterator, Optional


def get_query(f: Any, cmd: str, value: Optional[str]) -> Iterator:
    data = map(lambda v: v.strip(), f)
    if cmd == "filter":
        return filter(lambda v: value in v, data)
    elif cmd == "map" and value is not None:
        id_ = int(value)
        return map(lambda v: v.split(" ")[id_], data)
    elif cmd == "unique":
        return iter(set(data))
    elif cmd == "sort":
        reverse = value == "desc"
        return iter(sorted(data, reverse=reverse))
    elif cmd == "limit" and value is not None:
        return get_limit(data, int(value))
    elif cmd == "regex":
        return filter(lambda v: re.findall(value, v), data)
    return data


def get_limit(data: Iterator, value: int) -> Iterator:
    count = 0
    for item in data:
        if count < value:
            yield item
        else:
            break
        count += 1
