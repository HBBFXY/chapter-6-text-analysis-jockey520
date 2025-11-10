def analyze_text(text):

    # 创建字典统计字符频率
    freq_dict = {}
    

    for char in text:

        if char.isalpha():

            char_lower = char.lower()
            freq_dict[char_lower] = freq_dict.get(char_lower, 0) + 1
    
    sorted_chars = sorted(freq_dict.keys(), key=lambda x: (-freq_dict[x], x))
    
    return sorted_chars

def print_char_frequency(text):

    sorted_chars = analyze_text(text)
    
    if not sorted_chars:
        print("文本中没有字母字符")
        return
    
    # 重新统计频率用于显示
    freq_dict = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            freq_dict[char_lower] = freq_dict.get(char_lower, 0) + 1
    
    print(f"文本: \"{text}\"")
    print("字符频率分析结果（降序排列）:")
    print("-" * 40)
    
    for char in sorted_chars:
        frequency = freq_dict[char]
        print(f"字符 '{char}': 出现 {frequency} 次")

def main():
    
    while True:
        print("\n请输入要分析的文本（输入空行退出）:")
        user_input = input().strip()
        
        if not user_input:
            print("程序结束，谢谢使用！")
            break
        
        print_char_frequency(user_input)



if __name__ == "__main__":
    # 运行测试
    test_analyze_text()
    
    # 运行交互式程序
    main()
