
def sum_odd_index (lst):
    s = 0
    for i in range (len(lst)):
        if i % 2  != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = [2, 3, 5, 9, 3]
sum_odd_index(lst)
