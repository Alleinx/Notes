# This program demonstrate the usage of Keyword-Only Arguments

def safe_division_c(number, divisior, *, ignore_overflow=False, ignore_zero_division=False):
    '''
    keyword-only arguments
    '''
    try:
        return number / divisior
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise OverflowError('inf')
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise ZeroDivisionError('divide 0')

def safe_division(number, divisior, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number / divisior
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise OverflowError('inf')
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise ZeroDivisionError('divide 0')

# non keyword-only arguments:
result = safe_division(1, 100, True, False)
print(result)

result = safe_division(1, 100, ignore_overflow=False, ignore_zero_division=True)
print(result)

# keyword-only arguments:
result = safe_division_c(1, 100, ignore_overflow=True, ignore_zero_division=True)
print(result)

# Error
result = safe_division_c(1, 100, True, False)
