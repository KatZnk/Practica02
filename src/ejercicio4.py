def validar_email(email):
    posA = email.find('@')
    posP = email.rfind('.')

    if (email.count('@') == 1 and 
        not email.startswith(('@','.')) and 
        not email.endswith(('@','.')) and 
        (posP > posA) and 
        (len(email) - posP > 2)):
        
        print('El email es válido.')
    else:
        print('El email no es válido.')