# Напишите программу, в которой указан список целых чисел. Замените
# отрицательные на -1, положительные на 1, и оставить ноль без
# изменений.(Используйте встроенные функции, чтобы решить эту задачу)


nums = [1, 2, 3, -7, -5, 0, -8]

for i in range(len(nums)):
    if nums[i] > 0:
        nums[i] = 1
    
    elif nums[i] < 0:
        nums[i] = -1
    
    else:
        nums[i] = 0
print(nums)





