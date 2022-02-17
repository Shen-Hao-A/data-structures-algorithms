'''
Author: shenhao
Date: 2022-02-16 20:29:12
LastEditors: shenhao
LastEditTime: 2022-02-16 20:33:13
Description: file content
FilePath: \grokking_algorithms-master\03_recursion\python\01_countdown.py
'''
def countdown(i):
  print(i)
  # base case
  if i <= 0:
    return
  # recursive case
  else:
    countdown(i-1)

countdown(5)
