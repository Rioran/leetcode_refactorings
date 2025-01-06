"""
Leetcode task:

Given a string text and an integer char_distance,
rearrange text such that the same characters are at least distance char_distance from each other.
If it is not possible to rearrange the string, return an empty string "".
"""
from collections import Counter


def get_decreasing_char_occurences(char_counter: Counter) -> list[tuple[int, str]]:
    return sorted([(occurrences, char) for char, occurrences in char_counter.items()], reverse=True)


def spread_char_across_slots(char_slots, char):
    for i in range(len(char_slots)):
        char_slots[i] += char


def spread_char_consequently(char_slots, slot, char, occurrences):
    current_slot = slot

    for _ in range(occurrences):
        current_slot = current_slot % (len(char_slots) - 1)
        char_slots[current_slot] = char_slots[current_slot] + char
        current_slot += 1

    return current_slot


def detect_slots_overflow(char_slots, char_distance):
    return any(map(lambda x: len(x) < char_distance, char_slots[:-1]))


def spread_chars(char_slots, decreasing_char_occurences):
    slot = 0
    top_occurrence = len(char_slots)

    for occurrences, char in decreasing_char_occurences:
        if occurrences == top_occurrence:
            spread_char_across_slots(char_slots, char)
        else:
            slot = spread_char_consequently(char_slots, slot, char, occurrences)


class Solution:
    def rearrangeString(self, text: str, char_distance: int) -> str:
        counter = Counter(text)
        decreasing_char_occurences = get_decreasing_char_occurences(counter)
        char_slots = [""] * decreasing_char_occurences[0][0]

        spread_chars(char_slots, decreasing_char_occurences)

        if detect_slots_overflow(char_slots, char_distance):
            return ""

        return "".join(char_slots)
