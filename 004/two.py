passports = []
with open('input.txt') as f:
    for line in f:
        value = line.split()
        passports.append(value)
f.close()

## Clean up passport entries
clean_passports = []
pass_dict = {}
i=0
while (i<len(passports)):
# while (i<17):
    for field in passports[i]:
        test = field.split(":")
        pass_dict[test[0]] = test[1]
    if len(passports[i]) == 0:
        pass_dict_copy = pass_dict.copy()
        clean_passports.append(pass_dict_copy)
        pass_dict.clear()
    i += 1

# print("# of clean passports: " + str(len(clean_passports)))

total_valid_points = 0
but_like_actually_valid = 0

valid_length = []

k=0
for passport in clean_passports:
    if ((len(clean_passports[k]) == 7) and 'cid' not in clean_passports[k]) or len(clean_passports[k]) == 8:
        valid_length.append(clean_passports[k])
    k += 1


print("Passports with valid length or only mising cid: " + str(len(valid_length)))

j=0
for items in clean_passports:

# Check for valid birth year 
    if "byr" in clean_passports[j]:
        if 1920 <= int(clean_passports[j]['byr']) <= 2002:
            # print("byr between 1920 and 2002: " + str(clean_passports[j]['byr']))
            total_valid_points += 1
        else:
            # print("Birthyear invalid: " + str(clean_passports[j]['byr']))
            total_valid_points += 0

    # Check for issue year 
    if "iyr" in clean_passports[j]:
        # print("Found a issue year field" )
        if 2010 <= int(clean_passports[j]['iyr']) <= 2020:
            # print("iyr between 2010 and 2020: " + str(clean_passports[j]['iyr']))
            total_valid_points += 1
        else:
            # print("Issue year invalid: " + str(clean_passports[j]['iyr']))
            total_valid_points += 0
            
    # Check for expiration year 
    if "eyr" in clean_passports[j]:
        if 2020 <= int(clean_passports[j]['eyr']) <= 2030:
            # print("eyr between 2010 and 2020: " + str(clean_passports[j]['eyr']))
            total_valid_points += 1
        else:
            # print("Exp year invalid: " + str(clean_passports[j]['eyr']))
            total_valid_points += 0
    
    # Check valid height
    if "hgt" in clean_passports[j]:
        if clean_passports[j]['hgt'][-2:] == "cm":
            if 150 <= int(clean_passports[j]['hgt'][:-2]) <= 193:
                # print("This is a valid cm height: " + str(clean_passports[j]['hgt']))
                total_valid_points += 1
                # print(clean_passports[j]['hgt'][:-2])
            else:
                # print("Nooope not a valid cm height sorry: " + str(clean_passports[j]['hgt']))
                total_valid_points += 0
        elif clean_passports[j]['hgt'][-2:] == "in":
            if 59 <= int(clean_passports[j]['hgt'][:-2]) <= 76:
                # print("This is a valid in height: " + str(clean_passports[j]['hgt']))
                total_valid_points += 1
                # print(clean_passports[j]['hgt'][:-2])
            else:
                # print("Wrong number of inches: " + str(clean_passports[j]['hgt']))
                total_valid_points += 0

    # Check for valid eye color 
    valid_eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if "ecl" in clean_passports[j]:
        if clean_passports[j]['ecl'] in valid_eyes:
            # print("Found a valid eye color: " + clean_passports[j]['ecl'])
            total_valid_points += 1
        else:
            # print("Invalid eyes: " + clean_passports[j]['ecl'])
            total_valid_points += 0

    # Check for vaid hair color 
    if "hcl" in clean_passports[j] and len(clean_passports[j]['hcl']) == 7 and clean_passports[j]['hcl'][0] == "#":
        # print("We found a 7 digit with # first letter")

        hex_value = clean_passports[j]['hcl'][1:]
        # print(hex_value)
        
        ok_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

        matched_list = [characters in ok_chars for characters in hex_value]
        # print(matched_list)

        if all(matched_list) == True:
            # print("Looks like they were all correct")
            total_valid_points += 1
        else:
            # print("Not a valid hair color: " + clean_passports[j]['hcl'])
            total_valid_points += 0

    # Check for vaid passport number
    if "pid" in clean_passports[j] and len(clean_passports[j]['pid']) == 9:
        # print("We found a 9 digit pid")
        try:
            int(clean_passports[j]['pid'])
            total_valid_points += 1
            # print("PID can be converted to int.")
        except:
            total_valid_points += 0
            # print("That's like not even a number")

    # print("Totally valid thoooo: " + str(total_valid_points))    
    if total_valid_points >= 7:
        but_like_actually_valid += 1
        # print("But like actually valid on line " + str(j) + ": " + str(but_like_actually_valid))
    total_valid_points = 0
    j += 1

# print(valid_length[-1])
print("Total valid number: " + str(but_like_actually_valid))