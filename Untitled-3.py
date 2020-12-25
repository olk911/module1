def sort_list(my_list, direction=None): # def - оператор создания функции
                                        # параметр my_list - список значений
                                        # параметр direction - специальный, определяет направление сортировки, может быть 1 или -1
    if direction:
        for i in range(len(my_list)):  # len - число элементов в контейнере
            for j in range(i, len(my_list)):
                if (direction == -1 and my_list[i] > my_list[j]) or (direction == 1 and my_list[i] < my_list[j]):
                    temp = my_list[i]
                    my_list[i] = my_list[j]
                    my_list[j] = temp
                    print(temp)

    print(my_list)

new_list = [1, 0, 5, 4]
i=0
j=0

sort_list(new_list, -1)