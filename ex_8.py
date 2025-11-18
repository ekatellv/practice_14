def sorted_string(input_string: str) -> str:
    char_list = list(input_string)
    char_list.sort()
    result_string = ''.join(char_list)
    return result_string


def main():
    text = input('enter a string: ')
    print(sorted_string(text))


if __name__ == '__main__':
    main()
