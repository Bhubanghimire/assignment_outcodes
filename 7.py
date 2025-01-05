from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    # Frequency count of characters in t
    t_count = Counter(t)
    required = len(t_count)

    # Sliding window
    left, right = 0, 0
    window_counts = {}
    formed = 0

    # Result variables
    min_length = float("inf")
    start = 0

    while right < len(s):
        # Add character from the right pointer
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if the character satisfies the frequency requirement
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        # Try to contract the window until it's no longer valid
        while left <= right and formed == required:
            char = s[left]

            # Update result if a smaller window is found
            if right - left + 1 < min_length:
                min_length = right - left + 1
                start = left

            # Remove the left character from the window
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1

            left += 1

        # Expand the window
        right += 1

    # Return the minimum window substring
    return s[start:start + min_length] if min_length != float("inf") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  # Output: "BANC"
