#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    def count_vowels(input_string):
        vowels = set("aeiouAEIOU")
        vowel_count = sum(1 for char in input_string if char in vowels)
        return vowel_count

    user_input = input("Введите строку: ")
    result = count_vowels(user_input)

    print(f"Количество гласных в строке: {result}")

