def is_valid_passport(passport):
    keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    fields = [couple.split(':') for couple in passport.split(' ')]
    passkeys = set([couple[0] for couple in fields])
    passkeys.add('cid')
    return passkeys == keys

def count_valid_passports(file):
    file = open(file, 'r')
    lines = [line.rstrip('\n') for line in file.readlines()]
    passport, passports, checklist = '', [], []
    for line in lines:
        if line:
            # print('yes')
            passport += f'{line} '
            # print(passport)
        else:
            passports.append(passport.rstrip(' '))
            passport = ''
    passports.append(passport.rstrip(' '))
    for passport in passports:
        checklist.append(is_valid_passport(passport))
    return sum(checklist)

print(count_valid_passports('passports02.txt'))
