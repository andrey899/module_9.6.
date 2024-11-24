#                     pаботa с функциями генераторами и оператором yield
#                                   Задача:
#   Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
#    при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

# Напишите функцию-генератор all_variants(text).
def all_variants(text):
    # Опишите логику работы внутри функции all_variants.
    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[i:j + i + 1]


# Вызовите функцию all_variants и выполните итерации.

sum = all_variants("abc")
for i in sum:
    print(i)