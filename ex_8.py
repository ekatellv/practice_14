def sorted_string(input_string: str) -> str:
    """
    Sorts the characters of a string in ascending order and returns the sorted string.
    
    Args:
        input_string (str): The string to be sorted
        
    Returns:
        str: A new string with characters sorted in ascending order
    """
    
    char_list = list(input_string)
    char_list.sort()
    result_string = ''.join(char_list)
    return result_string


def main():
    text = input('enter a string: ')
    print(sorted_string(text))


if __name__ == '__main__':
    main()
