def process(file):
    file = open(file, 'r')
    lines = [line.rstrip('\n') for line in file.readlines()]
    passports = []
    passport = ''
    for line in lines:
        if line:
            # print('yes')
            passport += f'{line} '
            # print(passport)
        else:
            passports.append(passport.rstrip(' '))
            passport = ''
    for passport in passports:
        checklist.append(is_valid_passport(passport))
    return sum(checklist)
process('passports02.txt')
