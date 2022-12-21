from typing import Sequence, Union, Any


__all__ = ('binary_search',)


def binary_search(struct: Sequence[Any], target: Any) -> Union[int, None]:
    left, right = 0, len(struct) - 1
    while left <= right:
        # choose middle element
        mid = struct[(left + right) // 2]

        # if found return index
        if mid == target:
            return (left + right) // 2

        # if mid < target then target might be to the right
        elif mid < target:
            left = (left + right) // 2 + 1

        # if mid < target then target might be to the left
        else:
            right = (left + right) // 2 - 1

    return None

