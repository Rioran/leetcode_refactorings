"""
Leetcode task:

Given a string text and an integer char_distance,
rearrange text such that the same characters are at least distance char_distance from each other.
If it is not possible to rearrange the string, return an empty string "".
"""
from collections import Counter


def get_increasing_char_occurences(char_counter: Counter) -> list[tuple[int, str]]:
    return sorted([(occurrences, char) for char, occurrences in char_counter.items()])


class Solution:
    def rearrangeString(self, text: str, char_distance: int) -> str:
        counter = Counter(text)
        increasing_char_occurences = get_increasing_char_occurences(counter)
        maxFreq = increasing_char_occurences[-1][0]
        slots = ["" for _ in range(maxFreq)]

        slot = 0
        while (increasing_char_occurences):
            freq, ch = increasing_char_occurences.pop()
            if (freq == maxFreq):
                for i in range(maxFreq):
                    slots[i] = slots[i] + ch
            else:
                while (freq):
                    slot = slot % (maxFreq - 1)
                    slots[slot] = slots[slot] + ch
                    freq -= 1
                    slot += 1
        for i in range(maxFreq - 1):  # up until last slot
            if len(slots[i]) < char_distance:
                return ""
        return "".join(slots)
