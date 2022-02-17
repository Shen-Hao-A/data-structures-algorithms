'''
Author: shenhao
Date: 2022-02-16 20:29:12
LastEditors: shenhao
LastEditTime: 2022-02-16 20:34:21
Description: file content
FilePath: \grokking_algorithms-master\04_quicksort\python\01_loop_sum.py
'''
def sum(arr):
  total = 0
  for x in arr:
    total += x
  return total

print(sum([1, 2, 3, 4]))
