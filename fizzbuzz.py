#
# for number in range(0, 100):
#     if number%3==0 and number%5==0:
#         print('fizzbuzz')
#     elif number%3==0:
#         print('fizz')
#     elif number%5==0:
#         print('buzz')
#     else:
#         print(number)
# print('end')

# Константы для делителей
FIZZ_DIVISOR = 3
BUZZ_DIVISOR = 5

# Основной цикл от 0 до 99 включительно
for number in range(100):
    output = ""

    if number % FIZZ_DIVISOR == 0:
        output += "fizz"
    if number % BUZZ_DIVISOR == 0:
        output += "buzz"

    # Если ни одно из условий не выполнено, печатаем число
    if output == "":
        output = number

    print(output)

print("end")
