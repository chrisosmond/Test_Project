import Backpack as bp

ListOfNumbers = []
while True:
    Number = int(input("Add a number to the list: "))
    if Number == 0:
        break
    ListOfNumbers.append(Number)


print(ListOfNumbers)
ListOfNumbers.sort()
print(ListOfNumbers)
Max_value = max(ListOfNumbers)
Dupes = bp.DupeRepeat(ListOfNumbers)
print(Dupes)