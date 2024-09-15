import base64

from solutions.solution import swap_k_groups


def ceil_div(x: int, a: int):
    """Equivalent to ceil(x / a)"""
    return (x + a - 1) // a


enc = "hkdHBzej8vJ3d3fil/ZXR1cmVuI29tbydxZHNobzZ9NGFXdDd5N1doU2FQA="
enc_bytes = base64.b64decode(enc)

for k in range(33):
    arr = [int.from_bytes(enc_bytes[i : i + 4], "little") for i in range(0, len(enc_bytes), 4)]
    assert len(arr) == ceil_div(len(enc_bytes), 4)

    res = list(map(lambda x: swap_k_groups(x, k), arr))
    res_bytes = b"".join(map(lambda x: x.to_bytes(4, "little"), res))
    if res_bytes.startswith(b"https://"):
        print("found k=", k)
        print(res_bytes.decode())
