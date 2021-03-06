#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:14:01 2019

@author: asingh
"""

# Exercise 1
def size(aSet):
   """
   aSet is a collection of objects, which might be empty.
   Objects are assumed to be of the same type.
   """
# Here is a set of possible test cases to include in a black box test 
# suite. Indicate which of the following conditions would make a good black 
# box test suite for the function size by clicking on the appropriate 
# choice(s).

# Review: Black Box Test Suites
# Black-box testing is a method of software testing that tests the 
# functionality of an application. Recall from the lecture that a way to 
# think about black-box testing is to look at both:

# The possible paths through the specification.
# The possible boundary cases.
# Undoubtably many - if not all - of the listed tests look like they would 
# be pretty good for testing the function size. However, we want you to 
# think critically about the way size is specified - including possible 
# boundary cases - and pick a set of tests that adequately and fully tests 
# all paths and boundary conditions. Be sure the set of tests you pick does 
# not have extraneous, useless, or repetitive tests.
# Ans: empty set, set size of 1, set size greater than 1
   
# Exercise 2
def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
# Indicate which of the conditions below would combine to make a good black 
# box test suite for the function union by selecting the appropriate 
# choice(s).
# ans: all
# set1 is an empty set; set2 is an empty set
# set1 is an empty set; set2 is of size greater than or equal to 1
# set1 is of size greater than or equal to 1; set2 is an empty set
# set1 and set2 are both nonempty sets which do not contain any objects in 
# common
# set1 and set2 are both nonempty sets which contain objects in common

# Exercise 3
def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger

# Review: Glass Box Test Suites
# Recall from the lecture that a path-complete glass box test suite would 
# find test cases that go through every possible path in the code. This is 
# different from black-box testing, because in black-box testing you only 
# have the function specification. For glass-box testing, you actually know 
# how the function you are testing is defined. Thus you can use this 
# definition to figure out how many different paths through the code exist, 
# and then pick a test suite based on that knowledge.

# Undoubtably many - if not all - of the listed tests look like they would 
# be pretty good for testing the function maxOfThree. However, we want you 
# to think critically about the way maxOfThree is defined - including 
# possible boundary cases - and pick a set of tests that adequately and 
# fully tests all paths and boundary conditions. A good first step will be 
# to look at the function definition and figure out what paths through the 
# code exist. Then, look through the suggested test suites one test at a 
# time and see if the suite tests every single path.

# Assume that maxOfThree is called with numbers as arguments.
# Which of the following test suites would make a path-complete glass box 
# test suite for maxOfThree?
## need four paths to traverse through all possible paths through the
## function: 1) a>b, 2) a>b 3) a>b and c > bigger and 4) a>b and c > bigger

# Exercise 4
def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   if len(set1) == 0:
      return set2
   elif set1[0] in set2:
      return union(set1[1:], set2)
   else:
      return set1[0] + union(set1[1:], set2)

# Assume that union is called with strings as arguments.
# Please select the best glass box test suite for the function union from 
# the following options:
# ans :Test Suite D: union('','abc'), union('a','abc'), union('ab','abc'),
# union('d','abc') correct

# Exercise 5
def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      x = x - a
   return count

# Please select the best glass box test suite for the function foo from the
# following options.
foo(9, 7)
## ans Test Suite B: foo(10, 3), foo(1, 4), foo(10, 6) correct

# Exercise: integer division
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    while x >= a:
        count += 1
        x = x - a
    return count

# When we call
# print(integerDivision(5, 3))
# we get the following error message:

# File "temp.py", line 9, in integerDivision
#     count += 1
# UnboundLocalError: local variable 'count' referenced before assignment
# Your task is to modify the code for integerDivision so that this error 
# does not occur.
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

# Exercise 6
def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)

rem(2, 5)
rem(5, 5)
rem(7, 5)

# rem(x-a, a)
# return rem(x-a, a)

# Exercise 7

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)

# When we call f(3) we expect the result 6, but we get 0.
# When we call f(1) we expect the result 1, but we get 0.
# When we call f(0) we expect the result 1, but we get 0.
# Using this information, choose what line of code should 
# be changed from the following choices:

f(3)
# return n
# return 1

# Exceptions and assertions
## Q1
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
        
fancy_divide([0, 2, 4], 1) # 1, 0
fancy_divide([0, 2, 4], 4) # -1, 0
fancy_divide([0, 2, 4], 0) # 0, error

## Q2
def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")

fancy_divide([0, 2, 4], 1) # 1, 0
fancy_divide([0, 2, 4], 4) # 1, 0, 0
fancy_divide([0, 2, 4], 0) # -2, 0

def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

fancy_divide([0, 2, 4], 1) # 1, 0
fancy_divide([0, 2, 4], 4) # 1, 0, 0
fancy_divide([0, 2, 4], 0) # 0, -2

def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)

## Does this code print 0 when you call fancy_divide([0, 2, 4], 0)
fancy_divide([0, 2, 4], 0)
## answer: no
        
def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
        
## Does this print 0 when you call fancy_divide([0, 2, 4], 0)
fancy_divide([0, 2, 4], 0)
## answer: yes

## Exercise: simple divide
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]

#def simple_divide(item, denom):
#   return item / denom

fancy_divide([0, 2, 4], 0)

def simple_divide(item, denom):
    try: 
        return item / denom
    except ZeroDivisionError:
        return 0

fancy_divide([0, 2, 4], 0)

# Exercise 3
def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers 

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')

## 1. Does the try block throw (also known as raise) an exception?, No
## What is the name of the exception the code is trying to catch?
## ZeroDivisionError
## What is the output? Invalid maximum element
## Since we are dividing by the maximum element in a list of positive
## numbers, we know that normalize will return a value between 0 and 1. 
## What type of condition is this? post condition
## We also know the result is not meaningful when the maximum element is 0,
## so we want to ensure that the numbers in the list do not violate this. 
## What type of condition is this? pre condition

def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers        

## Which condition does the line assert(max_number != 0) correspond to?
## pre condition
## Which condition does the line assert(0.0 <= numbers[i] <= 1.0) 
## correspond to? post condition
## What does the function call normalize([0, 0, 0]) print out?
## Cannot divide by 0 (no quotes)

