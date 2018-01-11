#numbers = [1, 4, 10, -3, -8, 7, 15, 0, 31, 28, -10]
numbers =  [1, 9, -10, -20, -8, 7, 14, 0, 20, 20, -20]
def exam(lst):
 min_1 = min(lst[0], lst[1])
 max_1 = max(lst[0], lst[1])
 min_2 = lst[0] * lst[1]
 max_2 = lst[0] * lst[1]
 min_3 = lst[0] * lst[1] * lst[2]

 for x in lst[2:]:
   min_3 = min(min_3, x * min_2, x * max_2)
   max_2 = max(min_2, x * min_1, x * max_1)
   max_2 = min(max_2, x * min_1, x * max_1)
   min_1 = min(min_1, x)
   max_1 = max(max_1, x)
 return min_3

print(exam(numbers))
