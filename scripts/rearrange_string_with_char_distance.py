'''
Leetcode task:

Given a string s and an integer k,
rearrange s such that the same characters are at least distance k from each other.
If it is not possible to rearrange the string, return an empty string "".
'''
import collections


class Solution:
    def rearrangeString(self, text: str, char_distance: int) -> str:
        counter = collections.Counter(text)
        items = sorted([(freq, ch) for ch, freq in counter.items()])
        maxFreq = items[-1][0]
        slots = ["" for _ in range(maxFreq)]

        slot = 0
        while (items):
            freq, ch = items.pop()
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
