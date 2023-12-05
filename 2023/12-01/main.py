num_dict = {'one': 'o1e', 'two': 't2w', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n',
            'eight': 'e8t',
            'nine': 'n9e'}

def clean_code(code):
    nums = []
    for char in code:
        if char.isnumeric():
            nums.append(char)
    nums = "".join([nums[0], nums[-1]])
    return nums


with open('input.txt', 'r') as codes_txt:
    codes = [line.rstrip('\n') for line in codes_txt]

    for i, code in enumerate(codes):
        for word in num_dict:
            if word in code:
                code = code.replace(word, num_dict[word])
        codes[i] = code

    numbers = []
    for code in codes:
        numbers.append(int(clean_code(code)))

    result = 0
    for number in numbers:
        result += number

    print(result)

