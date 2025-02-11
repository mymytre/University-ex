def add_frac(frac1: list, frac2: list):
    if denominator_check(frac1, frac2):
        return "Error!!"
    elif frac1[1] == frac2[1]:
        return [frac1[0] + frac2[0], frac2[1]]
    else:
        out = [None] * 2
        out[1] = frac1[1] * frac2[1]
        out[0] = frac1[1] * frac2[0] + frac1[0] * frac2[1]
        return out


def sub_frac(frac1: list, frac2: list):
    if denominator_check(frac1, frac2):
        return "Error!!"
    elif frac1[1] == frac2[1]:
        return [frac1[0] - frac2[0], frac2[1]]
    else:
        out = [None] * 2
        out[1] = frac1[1] * frac2[1]
        out[0] = frac1[0] * frac2[1] - frac1[1] * frac2[0]
        return out


def mul_frac(frac1: list, frac2: list):
    if denominator_check(frac1, frac2):
        return "Error!!"
    else:
        return [frac1[0] * frac2[0], frac1[1] * frac2[1]]


def div_frac(frac1: list, frac2: list):
    if denominator_check(frac1, frac2):
        return "Error!!"
    else:
        return [frac1[0] * frac2[1], frac1[1] * frac2[0]]


def is_positive(frac: list):
    if frac[1] == 0:
        return "Error!!"
    elif positive_check(frac):
        return True
    else:
        return False


def positive_check(frac: list):
    return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)


def is_zero(frac: list):
    if frac[1] == 0:
        return "Error!!"
    else:
        return frac[0] == 0


def cmp_frac(frac1: list, frac2: list):
    if denominator_check(frac1, frac2):
        return "Error!!"
    elif frac1[0] / frac1[1] > frac2[0] / frac2[1]:
        return 1
    elif frac1[0] / frac1[1] < frac2[0] / frac2[1]:
        return -1
    else:
        return 0


def frac2float(frac):
    if frac[1] == 0:
        return "Error!!"
    else:
        return float(frac[0] / frac[1])


def denominator_check(frac1, frac2):
    return frac1[1] == 0 or frac2[1] == 0
