from typing import Callable, List, TypeVar

T = TypeVar('T')


def binary_search_int(left: int, right: int, f: Callable[[int], int]) -> int:
    """
    Finds the greatest x such that f(x) <= 0
    invariant: f(right) > 0, f(left) <= 0
    """
    while right - left > 1:
        mid = (left + right) // 2
        if f(mid) > 0:
            right = mid
        else:
            left = mid
    return left


def binary_search_float(left: float, right: float, f: Callable[[float], float], eps: float) -> float:
    """
    Finds the greatest x such that f(x) <= 0 with precision eps.
    invariant: f(right) > 0, f(left) <= 0
    """
    if eps < 1.7 * 1e-308:
        raise ArithmeticError("Precision is too high, python can't store such values")
    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) > 0:
            right = mid
        else:
            left = mid
    return left


def binary_search_array(a: List[T], left=0, right=None, f=lambda x: x) -> int:
    """
    Finds the greatest index such that f(a[index]) <= 0 and left < index <= right.
    invariant: f(a[left]) <= 0, f(a[right]) > 0 or a[right] is not defined.
    default arguments: left = 0, right = len(a), f(x) returns x
    """
    if right is None:
        right = len(a)
    while right - left > 1:
        mid = (left + right) // 2
        if f(a[mid]) > 0:
            right = mid
        else:
            left = mid
    return left
