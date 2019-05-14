from typing import List


class Solution:

    MORSE_WORDS = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                   "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                   "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                   "-.--", "--.."]

    def get_morse_word(self, word: str) -> str:
        return "".join([self.MORSE_WORDS[ord(ch) - ord("a")] for ch in word])

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        words = [self.get_morse_word(word) for word in words]
        return len(set(words))
