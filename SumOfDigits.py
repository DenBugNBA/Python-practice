num = int(input("Введите число: "))

sum = 0

while num > 0:
    sum += num % 10
    num //= 10
print("Сумма всех цифр: " + str(sum))
