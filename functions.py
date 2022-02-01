def cleanup(string):
    """Sterge spatile de la inceput si sfarsit
    Transforma stringul in formatul prima litera mare, urmatoarele mici
    Returneaza stringul
    :param string: un string care va fi transformate
    :returns: stringul fara spatii si cu prima litera mare
    """
    new_string = string.strip()  # elimina spatile de la inceput si sfarsit
    new_string = new_string.capitalize()
    return string


def newf(first, second):
    """Adds two value
    Parameters
        first: primul parametru care va fi adunat  
        second: al doilea parametru care va fi adunat
    Returns:
        Suma celor doi parametrii

    """
    return first + second


print(cleanup(" text de transformat"))
print(cleanup('test'))
print(cleanup('un text'))
print(cleanup("un text de schimbat in functia cleanup"))
print(cleanup.__doc__)
help(cleanup)
help(add)