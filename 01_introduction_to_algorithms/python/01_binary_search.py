'''
Author: shenhao
Date: 2022-02-16 20:29:12
LastEditors: shenhao
LastEditTime: 2022-02-17 14:03:43
Description: file content
FilePath: \data structures and algorithms\01_introduction_to_algorithms\python\01_binary_search.py
'''
def binary_search(list, item):
  """
  从某一顺序列表中返回所查找数字的索引,若列表中不存在该数字,则返回None
    Args:
        list (_type_): 顺序列表
        item (_type_): 所查找数字

    Returns:
        _type_: 所查找数字在list中的索引,索引从0开始,若列表中不存在该数字,则返回None
    """
  # low and high keep track of which part of the list you'll search in.
  low = 0
  high = len(list) - 1

  # While you haven't narrowed it down to one element ...
  while low <= high:
    # ... check the middle element， //表示整除
    mid = (low + high) // 2
    guess = list[mid]
    # Found the item.
    if guess == item:
      return mid
    # The guess was too high.
    if guess > item:
      high = mid - 1
    # The guess was too low.
    else:
      low = mid + 1

  # Item doesn't exist
  return None

my_list = [1, 3, 5, 7, 9, 10, 11]
print(binary_search(my_list, 9)) # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print(binary_search(my_list, -1)) # => None
