def analyze_char_frequency(input_str):

    frequency = {}

    for char in input_str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    sorted_chars = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    print("字符出现频率（降序）：")
    for char, count in sorted_chars:
        print(f"'{char}': {count}次")

user_input = input("请输入一个字符串：")

analyze_char_frequency(user_input)
