def is_valid_password(password, settings):
    set = [s.split(' ') for s in settings.split('-')]
    test1 = password[int(set[0][0]) - 1] == set[1][1]
    test2 = password[int(set[1][0]) - 1] == set[1][1]
    return(test1 ^ test2)
