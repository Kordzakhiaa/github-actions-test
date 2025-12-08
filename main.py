def simple_func(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")
    return n + 1 == 2
