def is_valid_passport(passport):
    keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    fields = [couple.split(':') for couple in passport.split(' ')]
    passkeys = set([couple[0] for couple in fields])
    passkeys.add('cid')
    allowedhcl = set('0123456789abcdef#')
    allowedecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if passkeys != keys:
        return False

    for field in fields:
        if field[0] == 'byr':
            if int(field[1]) < 1920 or int(field[1]) > 2020:
                return False
        elif field[0] == 'iyr':
            if int(field[1]) < 2010 or int(field[1]) > 2020:
                return False
        elif field[0] == 'eyr':
            if int(field[1]) < 2020 or int(field[1]) > 2030:
                return False
        elif field[0] == 'hgt':
            if field[1][-2:] == 'cm':
                if int(field[1][:-2]) < 150 or int(field[1][:-2]) > 193:
                    return False
            elif field[1][-2:] == 'in':
                if int(field[1][:-2]) < 59 or int(field[1][:-2]) > 76:
                    return False
            else:
                return False
        elif field[0] == 'hcl':
            if field[1][0] != '#':
                return False
            elif len(field[1]) != 7:
                return False
            elif not set(field[1]).issubset(allowedhcl):
                return False
        elif field[0] == 'ecl':
            if field[1] not in allowedecl:
                return False
        elif field[0] == 'pid':
            if len(field[1]) != 9:
                return False
        return True

    # voorwaarden

def count_valid_passports(file):
    file = open(file, 'r')
    lines = [line.rstrip('\n') for line in file.readlines()]
    passport, passports, checklist = '', [], []

    for line in lines:
        if line:
            passport += f'{line} '
        else:
            passports.append(passport.rstrip(' '))
            passport = ''

    passports.append(passport.rstrip(' '))

    for passport in passports:
        checklist.append(is_valid_passport(passport))

    return sum(checklist)

print(count_valid_passports('passports02.txt'))
