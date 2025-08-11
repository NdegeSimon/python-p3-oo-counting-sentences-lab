#!/usr/bin/env python3

# lib/my_string.py
import re

class MyString:
    def __init__(self, value=""):
        self.value = value  # Uses the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        # Split on ., ?, or ! (one or more in a row)
        parts = re.split(r'[.!?]+', self.value)
        # Remove empty strings and strip whitespace
        sentences = [p.strip() for p in parts if p.strip()]
        return len(sentences)
