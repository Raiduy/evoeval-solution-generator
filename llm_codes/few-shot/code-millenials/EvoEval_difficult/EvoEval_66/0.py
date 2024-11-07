def advancedDigitSum(s, t):
    sum_s = sum(ord(ch) for ch in s if ch.isupper())
    sum_t = sum(ord(ch) for ch in t if ch.islower())
    return (sum_s, sum_t)