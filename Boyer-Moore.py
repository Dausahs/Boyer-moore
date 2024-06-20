def bad_character_heuristic(pattern):
    """
    Preprocesses the pattern to create the bad character heuristic table.
    """
    bad_char_table = [-1] * 256
    for i in range(len(pattern)):
        bad_char_table[ord(pattern[i])] = i
    return bad_char_table

def good_suffix_heuristic(pattern):
    """
    Preprocesses the pattern to create the good suffix heuristic tables.
    """
    m = len(pattern)
    good_suffix_table = [0] * (m + 1)
    border_pos_table = [0] * (m + 1)

    i = m
    j = m + 1
    border_pos_table[i] = j

    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if good_suffix_table[j] == 0:
                good_suffix_table[j] = j - i
            j = border_pos_table[j]
        i -= 1
        j -= 1
        border_pos_table[i] = j

    j = border_pos_table[0]
    for i in range(m + 1):
        if good_suffix_table[i] == 0:
            good_suffix_table[i] = j
        if i == j:
            j = border_pos_table[j]

    return good_suffix_table

def boyer_moore_search(text, pattern):
    """
    Searches for occurrences of the pattern in the text using the Boyer-Moore algorithm.
    """
    m = len(pattern)
    n = len(text)
    
    bad_char_table = bad_character_heuristic(pattern)
    good_suffix_table = good_suffix_heuristic(pattern)

    s = 0
    matches = []
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            matches.append(s)
            s += good_suffix_table[0]
        else:
            s += max(good_suffix_table[j + 1], j - bad_char_table[ord(text[s + j])])
    
    return matches

# Example usage
text = " Find the pattern with spaces"
pattern = "pattern with"
matches = boyer_moore_search(text, pattern)
print("Pattern found at positions:", matches)  # Expected: [10]



