def convert_to_base(num, base):
    result = ""
    while num > 0:
        remainder = num % base
        result = str(remainder) + result
        num //= base
    return result if result != "" else "0"

def answer(n, b):
    k = len(n)
    seen = {}

    while n not in seen:
        seen[n] = len(seen)
        x = int(''.join(sorted(n, reverse=True)), base=b)
        y = int(''.join(sorted(n)), base=b)
        z = x - y
        n = convert_to_base(z, b).zfill(k)

    return len(seen) - seen[n]