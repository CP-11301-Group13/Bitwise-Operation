import base64

from solutions.solution import swap_k_groups


def ceil_div(x: int, a: int):
    """Equivalent to ceil(x / a)"""
    return (x + a - 1) // a


k = 4  # k has to be divisor of 32, otherwise information will be lost
data = b"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
data += b"\x00" * (ceil_div(len(data), 4) * 4 - len(data))
arr = [int.from_bytes(data[i : i + 4], "little") for i in range(0, len(data), 4)]
assert len(arr) == ceil_div(len(data), 4)

encoded = list(map(lambda x: swap_k_groups(x, k), arr))
assert list(map(lambda x: swap_k_groups(x, k), encoded)) == arr

encoded_bytes = b"".join(map(lambda x: x.to_bytes(4, "little"), encoded))
assert len(encoded_bytes) == len(data)

print(hex(int.from_bytes(b"\xab\xcd\xef\x01", "little")))


print(base64.b64encode(encoded_bytes).decode())
