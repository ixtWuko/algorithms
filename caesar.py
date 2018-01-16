#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''a module to encode and decode caesar'''

def caesar_encode(string_to_encode, shift = 3):
    result = ''
    for char in string_to_encode:
        if char.isalpha():
            if char.islower():
                temp = (ord(char) - ord('a') + shift) % 26 + ord('a')
            else:
                temp = (ord(char) - ord('A') + shift) % 26 + ord('A')
            temp_char = chr(temp)
        else:
            temp_char = char
        result += temp_char
    return result

def casear_decode(string_to_decode, shift = 3):
    result = ''
    for char in string_to_decode:
        if char.isalpha():
            if char.islower():
                temp = (ord(char) - ord('a') - shift + 26) % 26 + ord('a')
            else:
                temp = (ord(char) - ord('A') - shift + 26) % 26 + ord('A')
            temp_char = chr(temp)
        else:
            temp_char = char
        result += temp_char
    return result

if __name__ == '__main__':
    print(caesar_encode("encode this string using caesar's encryption"))
    print(casear_decode("ghfrgh wklv vwulqj xvlqj fdhvdu'v hqfubswlrq"))