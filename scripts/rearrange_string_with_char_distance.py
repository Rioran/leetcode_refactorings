"""
Leetcode task:

Given a string text and an integer char_distance,
rearrange text such that the same characters are at least distance char_distance from each other.
If it is not possible to rearrange the string, return an empty string "".
"""
from collections import Counter


def get_increasing_char_occurences(char_counter: Counter) -> list[tuple[int, str]]:
    return sorted([(occurrences, char) for char, occurrences in char_counter.items()])


def spread_char_across_slots(char_slots, char, top_occurrence):
    for i in range(top_occurrence):
        char_slots[i] = char_slots[i] + char


def spread_char_consequently(char_slots, slot, char, occurrences, top_occurrence):
    while occurrences:
        slot = slot % (top_occurrence - 1)
        char_slots[slot] = char_slots[slot] + char
        occurrences -= 1
        slot += 1


class Solution:
    def rearrangeString(self, text: str, char_distance: int) -> str:
        counter = Counter(text)
        increasing_char_occurences = get_increasing_char_occurences(counter)
        top_occurrence = increasing_char_occurences[-1][0]
        char_slots = ["" for _ in range(top_occurrence)]

        slot = 0
        while increasing_char_occurences:
            occurrences, char = increasing_char_occurences.pop()
            if occurrences == top_occurrence:
                spread_char_across_slots(char_slots, char, top_occurrence)
            else:
                spread_char_consequently(char_slots, slot, char, occurrences, top_occurrence)
        for i in range(top_occurrence - 1):  # up until last slot
            if len(char_slots[i]) < char_distance:
                return ""
        return "".join(char_slots)
