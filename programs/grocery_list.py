"""
1. Insert item to buy and click enter
2. Afret inserted every of items to buy insert ctrl-d
3. See your grocery list

"""

list = []
while True:
    try:
        x = input().upper()
        list.append(x)
    except EOFError:
        break
list.sort()

list2 = []
try:
    el_str = str(1) + " " + list[0]
    list2.append(el_str)
except IndexError:
    pass

for el in list[1:]:
    indx = 1
    el_str = str(indx) + " " + str(el)

    if list2[-1][2:] !=  el_str[2:]:
        list2.append(el_str)
    else:
        indx = int(list2[-1][0]) + 1
        list2.remove(list2[-1])
        new_el_str = str(indx) + " " + str(el)
        list2.append(new_el_str)
print()

for el in list2:
    print(el)
