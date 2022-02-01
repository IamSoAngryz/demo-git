def cleanup(string):
    """Sterge spatile de la inceput si sfarsit
    Transforma stringul in formatul prima litera mare, urmatoarele mici
    Returneaza stringul
    """
    new_string = string.strip()
    new_string = new_string.capitalize()
    return string


print(cleanup( " text de transformat"))
print(cleanup('test'))
print(cleanup( 'un text'))