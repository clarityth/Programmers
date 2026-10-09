from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    ans = Fraction(numer, denom)
    return [ans.numerator, ans.denominator]