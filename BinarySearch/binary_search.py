from typing import Callable


def binary_search_int(left: int, right: int, f: Callable[[int], int]) -> int:
    """
    Finds the least x such that f(x) >= 0
    invariant: f(right) >= 0, f(left) < 0
    """
    while right - left > 1:
        mid = (left + right) / 2
        if f(mid) >= 0:
            right = mid
        else:
            left = mid
    return right


def binary_search_float(left: float, right: float, f: Callable[[float], float], eps: float) -> float:
    """
    Finds the least x such that f(x) >= 0 with precision eps.
    invariant: f(right) >= 0, f(left) < 0
    """
    if eps < 1.7 * 1e-308:
        raise ArithmeticError("Precision is too high, python can't store such values")
    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) >= 0:
            right = mid
        else:
            left = mid
    return right


