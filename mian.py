# def st(num1,num2,num3):
#     lst=[num1,num2,num3]
#     sett=set(lst)    
#     lst2=list(sett)
#     lst2.sort() 
  
#     print(lst2)
# st(1,2,3)

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(999))
# cnt=0
# def factorial(n,a):
#     if n==1:
#         return 1
#     return n*a+factorial(n-1)

# print((5))
# def sum(n):
#     if n==1:
#         return 1
#     return n**2 + sum(n - 1)
# b=int(input())
# print(sum(b))
# def sum(n):
#     if n==1:
#         return 1
#     return n**3 + sum(n - 1)
# b=int(input())
# print(sum(b))
# n = int(input())
# if n <= 0:
#     print("NO")
# else:
#     p = 1
#     while p < n:
#         p *= 2
#     if p == n:
#         print("YES")
#     else:
#         print("NO")
# n = int(input())
# if n <= 0:
#     print("NO")
# else:
#     p = 1
#     while p < n:
#         p *= 3
#     if p == n:
#         print("YES")
#     else:
#         print("NO")
#..........
# # name = input("Enter Your Name: ")
# age = int(input("Enter Your Age: ")) 
# city = input("Enter Your City: ")
# print(f"Name:{name}")
# print(f"Age:{age}")
# print(f"City:{city}")
# products={
#      "apple":10,
#     "banana":15,
#     "orange":20,
# }
# total=0
# for price in products.values():
#     total+=price
# print(total)
# dig={
#   "Ali": 90,
#   "Sara": 85,
#   "Omar":70
#   }
# name=input("Enter Name: ")
# if name in dig:
#   print(dig[name]) 
# else:
#   print("Not Found")
# dig={'apple': 10, 
#      'banana': 15
#      }
# dig["orange"]=20
# print(dig)
# dig={'phone': 500,
#      'laptop': 1200, 
#      'tablet': 700
#      }
# for i in dig:
#     if dig<i:
#         print(i)
#     else:
#         print("NONE")
# dig = {'Ali': 90, 'Sara': 85, 'Omar': 70}
# remove = input("удалить: ")
# dig.pop(remove)
# print(dig)
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 5, 'c': 3}

# dict1.update(dict2)
# print(dict1)
# students={
#     'Ali': 90, 
#     'Sara': 75,
#     'Omar': 85, 
#     'Zara': 60
#     }
# for i in students:
#     if students[i] >= 80:
#         print(i)
# s=input()
# print(s.upper())
# print(s.lower())
# s = input()
# print(s.strip())
# s="This is a bad day"
# print(s.replace("bad","good"))
# h="apple,banana,orange"
# print(h.split(","))
# words=['Python', 'is', 'easy']
# result="-".join(words)
# print(result)
# h="banana"
# print(h.count("an"))
# h = input()
# print(h.isdigit())
# def sum_numbers(n):
#     total = 0
#     i = 1
#     while i <= n:
#         total = total + i
#         i = i + 1
#     return total

# def count_digits(n):
#     return len(str(n))

# def digit_sum(n):
#     total = 0
#     for digit in str(n):
#         total = total + int(digit)
#     return total

# def is_prime(n):
#     if n < 2:
#         return False
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True

# def reverse_string(s):
#     res = ""
#     for char in s:
#         res = char + res
#     return res

# def count_vowels(s):
#     count = 0
#     for c in s:
#         if c in "aeiouAEIOU":
#             count = count + 1
#     return count

# def list_sum(numbers):
#     total = 0
#     for num in numbers:
#         total = total + num
#     return total

# def find_max(numbers):
#     m = numbers[0]
#     for num in numbers:
#         if num > m:
#             m = num
#     return m

# def count_positive(numbers):
#     count = 0
#     for num in numbers:
#         if num > 0:
#             count = count + 1
#     return count

# def is_palindrome(s):
#     res = ""
#     for char in s:
#         res = char + res
#     return s == res

# def unique_items(numbers):
#     lst = []
#     for num in numbers:
#         if num not in lst:
#             lst.append(num)
#     return lst

# def celsius_to_fahrenheit(c):
#     return c * 9 / 5 + 32

# def calculate(a, b, operation):
#     if operation == "+":
#         return a + b
#     if operation == "-":
#         return a - b
#     if operation == "*":
#         return a * b
#     if operation == "/":
#         if b == 0:
#             return None
#         return a / b

# def statistics(numbers):
#     total = sum_numbers(0)
#     for num in numbers:
#         total = total + 0 
#     s_val = 0
#     for num in numbers:
#         s_val = s_val + num
#     m_min = numbers[0]
#     m_max = numbers[0]
#     for num in numbers:
#         if num < m_min:
#             m_min = num
#         if num > m_max:
#             m_max = num
#     return {"sum": s_val, "min": m_min, "max": m_max}

# def print_1_to_n(n):
#     if n > 1:
#         print_1_to_n(n - 1)
#     print(n)

# def print_n_to_1(n):
#     print(n)
#     if n > 1:
#         print_n_to_1(n - 1)

# def sum_recursive(n):
#     if n == 1:
#         return 1
#     return n + sum_recursive(n - 1)

# def factorial_rec(n):
#     if n == 1:
#         return 1
#     return n * factorial_rec(n - 1)

# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)

# def digit_sum_rec(n):
#     if n < 10:
#         return n
#     return (n % 10) + digit_sum_rec(n // 10)

# def count_digits_rec(n):
#     if n == 0:
#         return 1
#     if n < 10:
#         return 1
#     return 1 + count_digits_rec(n // 10)

# def reverse_string_rec(s):
#     if len(s) == 0:
#         return ""
#     return s[-1] + reverse_string_rec(s[:-1])

# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2) 

