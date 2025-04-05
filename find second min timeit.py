import timeit

def find_min2(array):
  if len(array) < 2:
    return None

  min1 = float('inf')
  min2 = float('inf')

  for num in array:
    if num < min1:
      min2 = min1
      min1 = num
    elif num < min2 and num != min1:
      min2 = num

  return min2 if min2 != float('inf') else None

array = [8, 6, 4, 2, 5, 9, 4, 6, 5]
second_min = find_min2(array)
print(second_min)

number = 1000  
execution_time1 = timeit.timeit(lambda: find_min2(array), number=number)
print(f"time for end : {execution_time1:.6f} sec")
print(f"middle time: {execution_time1 / number:.9f} sec")
