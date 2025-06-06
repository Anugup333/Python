class AnujDivisionError(Exception):
    pass

def division(a,b):
    if b == 0:
        raise AnujDivisionError
    else:
        return a/b