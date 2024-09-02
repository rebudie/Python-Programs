roman = []

arabic = input("Максимально 3999: ")
while True:
    if int(arabic) < 1 or int(arabic) > 3999:
        print("Еблан(ка)? Еще раз: ")
        arabic = input("Максимально 3999: ")
    else:
        break

placeM = 0


def translator(number, place):
    if place == 0:
        if number == "1": roman.append("I")
        if number == "2": roman.append("II")
        if number == "3": roman.append("III")
        if number == "4": roman.append("IV")
        if number == "5": roman.append("V")
        if number == "6": roman.append("VI")
        if number == "7": roman.append("VII")
        if number == "8": roman.append("VIII")
        if number == "9": roman.append("IX")
    if place == 1:
        if number == "1": roman.append("X")
        if number == "2": roman.append("XX")
        if number == "3": roman.append("XXX")
        if number == "4": roman.append("XL")
        if number == "5": roman.append("L")
        if number == "6": roman.append("LX")
        if number == "7": roman.append("LXX")
        if number == "8": roman.append("LXXX")
        if number == "9": roman.append("XC")
    if place == 2:
        if number == "1": roman.append("C")
        if number == "2": roman.append("CC")
        if number == "3": roman.append("CCC")
        if number == "4": roman.append("CD")
        if number == "5": roman.append("D")
        if number == "6": roman.append("DC")
        if number == "7": roman.append("DCC")
        if number == "8": roman.append("DCCC")
        if number == "9": roman.append("CM")
    if place == 3:
        if number == "1": roman.append("M")
        if number == "2": roman.append("MM")
        if number == "3": roman.append("MMM")
    return 0


for i in range(len(arabic)):
    translator(arabic[len(arabic) - placeM - 1], placeM)
    placeM += 1

print("".join(reversed(roman)))