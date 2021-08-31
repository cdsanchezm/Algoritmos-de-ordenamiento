import random
import co.edu.unbosque.model.AG_Burbuja as bubble
import co.edu.unbosque.model.AG_Seleccion as sorting
import co.edu.unbosque.model.AG_MergeSort as mergeSort
import co.edu.unbosque.model.AG_QuickSort as quickSort
import co.edu.unbosque.model.AG_Radix as radix
import co.edu.unbosque.view.View as view
import time


def menu(totalNumbers, numbers, option):
    if option == 1:
        for x in range(totalNumbers):
            value = int(input("enter data --> "))
            numbers.append(value)
    if option == 2:
        case = view.caseList()
        if case == "1":
            for x in range(totalNumbers):
                numbers.append(x)
        if case == "2":
            for x in range(totalNumbers):
                a = random.randint(0, 4000000)
                numbers.append(a)
        if case == "3":
            for x in range(totalNumbers, 0, -1):
                numbers.append(x)

view.welcomePrint()
totalNumbers = int(input(" --> enter the total of numbers to order "))
numbers = []
option = int(view.optionNumbers())
menu(totalNumbers, numbers, option)
print("\n Plis select the algorithm to test :")

option = int(view.inputAlgorithm())

timestart = time.time()

if option == 1:
    print("you selected Bubble Ordering")
    bubble.ordenamientoBurbuja(numbers)

if option == 2:
    print("you selected Sorting Ordering")
    sorting.ordenamientoPorSeleccion(numbers)

if option == 3:
    print("you selected Radix Ordering ")
    radix.radix(totalNumbers, numbers)

if option == 4:
    print("you selected QuickSort Ordering")
    quickSort.quickSort(numbers)

if option == 5:
    print("you selected MergeSort Ordering")
    mergeSort.mergeSort(numbers)

if option >= 6:
    print("please select valid option ")

timeend = time.time()
print(timeend - timestart)
