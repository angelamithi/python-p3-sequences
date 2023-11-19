#!/usr/bin/env python3

def print_fibonacci(length):
     fib_sequence=[]
     a=0
     b=1
     for number in range(length):
          fib_sequence.append(a)
          a=b
          b=a+b
     print(fib_sequence)

print_fibonacci(8)