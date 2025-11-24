def count_hole_letters(text: str) -> tuple[int, int]:
    """
    Counts letters with holes and without holes in the given text.

    Args:
        text (str): Input text to analyze. Should contain lowercase letters and spaces.

    Returns:
        tuple[int, int]: A tuple containing:
            - hole_count: Number of letters with holes
            - no_hole_count: Number of letters without holes
    """
    hole_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}

    hole_count = 0
    no_hole_count = 0

    for char in text:
        if char.isalpha():
            if char in hole_letters:
                hole_count += 1
            else:
                no_hole_count += 1

    return hole_count, no_hole_count


def words_with_multiple_holes(text: str) -> list[str]:
    """
    Finds words containing two or more letters with holes.

    Args:
        text (str): Input text to analyze. Words should be space-separated.

    Returns:
        list[str]: List of words that contain two or more hole letters.
        Returns empty list if no words meet the criteria.
    """
    hole_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    words = text.split()
    result_words = []

    for word in words:
        hole_count_in_word = 0
        for char in word:
            if char in hole_letters:
                hole_count_in_word += 1
        if hole_count_in_word >= 2:
            result_words.append(word)

    return result_words


text = input('enter a sentence: ')

hole_count, no_hole_count = count_hole_letters(text)
print(f'letters with holes: {hole_count}')
print(f'letters without holes: {no_hole_count}')

words_with_holes = words_with_multiple_holes(text)
print(f'words with more than 1 hole: {words_with_holes}')
