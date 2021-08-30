import random

def radix(totalNumbers, numbers):
    maxLen = False
    tmp = -1
    location = 1

    while not maxLen:
        maxLen = True
        baskets = [list() for _ in range(totalNumbers)]

        for i in numbers:
            tmp = int(i / location)
            baskets[int(tmp % totalNumbers)].append(i)
            if maxLen and tmp > 0:
                maxLen = False

        a = 0
        for b in range(totalNumbers):
            basket = baskets[b]
            for i in basket:
                numbers[a] = i
                a += 1

        location *= totalNumbers
        print("baskets", baskets)

def menu(totalNumbers, numbers, option):
    if option == 1:
        for x in range(totalNumbers):
            value = int(input("enter data"))
            numbers.append(value)

    if option == 2:
        for x in range(totalNumbers):
            a = random.randint(0, 10000)
            numbers.append(a)

totalNumbers = int(input("---welcome to radix algorithm---\nenter the total of numbers to order"))
numbers = []
option = int(input(" 1) Manually enter numbers      2)generate numbers randomly"))
menu(totalNumbers,numbers,option)
totalNumbers = totalNumbers + 1
print(numbers)
radix(totalNumbers, numbers)
print(numbers)
