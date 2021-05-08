ROMAN_NUMS = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def get_sub_value(l1,l2):
    return ROMAN_NUMS[l2] - ROMAN_NUMS[l1]    

def roman_calculation(roman_word):
    """
    Convert Roman Numerals to Decimal Numerals
    """

    roman_list = list(roman_word.strip())
    cal = 0
    while roman_list:
        num1 = roman_list.pop(0)
        if roman_list and ROMAN_NUMS[num1] < ROMAN_NUMS[roman_list[0]]:
            num2 = roman_list.pop(0)
            cal += get_sub_value(num1,num2)
        else:
            cal += ROMAN_NUMS[num1]
    return cal

