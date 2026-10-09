"""
Задание 1. Расшифровка.

ИИ-ассистент выгрузил маркетинговый отчёт зашифрованным шифром Цезаря -
теперь его нужно расшифровать вручную.y
"""


def decode_caesar_cipher(text: str, shift: int) -> str:
    """
    Расшифровать text, зашифрованный шифром Цезаря со сдвигом shift.

    Каждая латинская буква в исходном (незашифрованном) тексте была сдвинута
    вперёд по алфавиту на shift позиций (с переходом с 'z' на 'a' и с 'Z' на 'A').
    Регистр буквы должен сохраняться. Все остальные символы - цифры, пробелы,
    знаки препинания - в тексте не менялись при шифровании и должны остаться
    как есть при расшифровке.

    Пример: decode_caesar_cipher("Khoor!", 3) -> "Hello!"
    """
    text_encoded = ''
    for i in text:
        if ord(i) >= 65 and ord(i) <= 90:
            decoded_symbol = chr((ord(i) - 65 - shift) % 26 + 65)
            text_encoded += decoded_symbol
        elif ord(i) >= 97 and ord(i) <= 122:
             decoded_symbol = chr((ord(i) - 97 - shift) % 26 + 97)
             text_encoded += decoded_symbol
        else:
            text_encoded += i
    return text_encoded
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("hw1-basics/data/task1_encoded.txt", encoding="utf-8") as f:
        encoded_text = f.read().strip()

    shift = 7
    print(decode_caesar_cipher(encoded_text, shift))
