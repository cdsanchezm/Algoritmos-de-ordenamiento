import random
import co.edu.unbosque.model.AG_Burbuja as bubble
import co.edu.unbosque.model.AG_Seleccion as sorting
import co.edu.unbosque.model.AG_MergeSort as mergeSort
import co.edu.unbosque.model.AG_QuickSort as quickSort
import co.edu.unbosque.model.AG_Radix as radix


def menu(totalNumbers, numbers, option):
    if option == 1:
        for x in range(totalNumbers):
            value = int(input("enter data --> "))
            numbers.append(value)

    if option == 2:
        for x in range(totalNumbers):
            a = random.randint(0, 10000)
            numbers.append(a)

print("----- Welcome to workshop 1 ----- \n"
      " >Cardenas Cortes Luis Esteban\n"
      " >Cristian David Sanchez Malagon"
      " \n >Andres Galvis Bolivar")

totalNumbers = int(input(" --> enter the total of numbers to order "))
numbers = []
option = int(input(" 1) Manually enter numbers      2)generate numbers randomly"))
menu(totalNumbers,numbers,option)
print("\n Plis select the algorithm to test :")

option = int(input(" 1) Bubble Ordering     2) Sorting Ordering \n"
                   " 3) Radix Ordering      4) QuickSort Ordering \n"
                   " 5) MergeSort Ordering  "))

if option == 1:
    print("you selected Bubble Ordering")
    print(numbers)
    bubble.ordenamientoBurbuja(numbers)
    print(numbers)
if option == 2:
    print("you selected Sorting Ordering")
    print(numbers)
    sorting.ordenamientoPorSeleccion(numbers)
    print(numbers)

if option == 3:
    print("you selected Radix Ordering ")
    print(numbers)
    radix.radix(numbers)
    print(numbers)

if option == 4:
    print("you selected QuickSort Ordering")
    print(numbers)
    quickSort.quickSort(numbers)
if option == 5:
    print("MergeSort Ordering")
    print(numbers)
    mergeSort.mergeSort(numbers)
if option >= 6:
    print("plis select valid option ")

