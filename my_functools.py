import functools

@functools.lru_cache(maxsize=5)
def calculate_square(n):
    print(f"Calculating square of {n}")
    return n ** 2

# Usage
for i in range(1, 8):
    result = calculate_square(i)
    print(f"Square of {i}: {result}")
    print(calculate_square.cache_info())
    print()