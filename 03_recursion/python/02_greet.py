'''
Author: shenhao
Date: 2022-02-16 20:29:12
LastEditors: shenhao
LastEditTime: 2022-02-16 20:33:50
Description: file content
FilePath: \grokking_algorithms-master\03_recursion\python\02_greet.py
'''
def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye!")

def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

greet("adit")
