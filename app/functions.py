def es_par(value):
    if value % 2 == 0:
        return True
    else:
        return False

def es_impar(value):
    if value % 2 == 0:
        return False
    else:
        return True

def es_alfanumerico(value):
    if value.isalnum() == True:
        return True
    else:
        return False