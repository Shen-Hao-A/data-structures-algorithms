'''
Author: shenhao
Date: 2022-02-16 20:29:12
LastEditors: shenhao
LastEditTime: 2022-02-16 20:34:07
Description: file content
FilePath: \grokking_algorithms-master\03_recursion\python\03_factorial.py
'''
def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print(fact(5))
