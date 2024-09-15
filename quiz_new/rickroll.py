import base64

from solutions.solution import swap_k_groups


def ceil_div(x: int, a: int):
    """Equivalent to ceil(x / a)"""
    return (x + a - 1) // a


data = b"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
data += b"\x00" * (ceil_div(len(data), 4) * 4 - len(data))
arr = [int.from_bytes(data[i : i + 4], "little") for i in range(0, len(data), 4)]
assert len(arr) == ceil_div(len(data), 4)

encoded = list(map(lambda x: swap_k_groups(x, 3), arr))
encoded_bytes = b"".join(map(lambda x: x.to_bytes(4, "little"), encoded))
assert len(encoded_bytes) == len(data)

print(base64.b64encode(encoded_bytes).decode())
