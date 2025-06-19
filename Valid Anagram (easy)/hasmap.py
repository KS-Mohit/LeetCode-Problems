def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}

    # Count characters in string s
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Subtract counts using string t
    for char in t:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False

    return True
