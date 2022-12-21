from binary_search import binary_search
from typing import Sequence, Any, Union


# for sorted in ascending order
def exponential_search(struct: Sequence[Any], target: Any) -> Union[int, None]:
    jump = 1
    # range for binary search
    while struct[jump] < target:
        jump *= 2

        if jump >= len(struct):
            break

    binary_search_result = binary_search(struct[jump // 2: jump + 1], target)

    # begin of range + offset or None
    return jump // 2 + binary_search_result if binary_search_result is not None else None


