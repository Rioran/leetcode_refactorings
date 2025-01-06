"""
Leetcode task:

Given a string text and an integer char_distance,
rearrange text such that the same characters are at least distance char_distance from each other.
If it is not possible to rearrange the string, return an empty string "".
"""
from collections import Counter


class CharSlots:
    def __init__(self, slots_count):
        self.slots_count = slots_count
        self.slots = [""] * slots_count
        self.current_slot = 0


def get_decreasing_char_occurences(text: str) -> list[tuple[int, str]]:
    return list(map(lambda x: x[::-1], Counter(text).most_common()))


def spread_char_consequently(char_slots: CharSlots, char, occurrences):
    current_slot = char_slots.current_slot
    dont_use_last_slot = char_slots.slots_count != occurrences

    for _ in range(occurrences):
        current_slot = current_slot % (char_slots.slots_count - dont_use_last_slot)
        char_slots.slots[current_slot] = char_slots.slots[current_slot] + char
        current_slot += 1

    char_slots.current_slot = current_slot


def detect_slots_overflow(char_slots, char_distance):
    return any(map(lambda x: len(x) < char_distance, char_slots[:-1]))


class Solution:
    def rearrangeString(self, text: str, char_distance: int) -> str:
        decreasing_char_occurences = get_decreasing_char_occurences(text)
        char_slots = CharSlots(slots_count=decreasing_char_occurences[0][0])

        for occurrences, char in decreasing_char_occurences:
            spread_char_consequently(char_slots, char, occurrences)

        if detect_slots_overflow(char_slots.slots, char_distance):
            return ""

        return "".join(char_slots.slots)
