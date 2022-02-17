'''
Author: shenhao
Date: 2022-02-16 20:29:12
LastEditors: shenhao
LastEditTime: 2022-02-16 20:36:03
Description: file content
FilePath: \grokking_algorithms-master\05_hash_tables\python\02_check_voter.py
'''
voted = {}
def check_voter(name):
  if voted.get(name):
    print("kick them out!")
  else:
    voted[name] = True
    print("let them vote!")

check_voter("tom")
check_voter("mike")
check_voter("mike")
