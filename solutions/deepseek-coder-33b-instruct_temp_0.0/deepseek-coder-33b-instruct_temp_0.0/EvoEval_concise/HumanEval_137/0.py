
def compare_one(a, b):
    if isinstance(a, str):
        a = float(a.replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace(',', '.'))
    if a == b:
        return None
    else:
        return max(a, b)