#task1************************************************************************
def duty_free(price, discount, holiday_cost):
  return holiday_cost//(price*discount*0.01)
#******************************************************************************

#task2
def str_count(strng, letter):
    return strng.count(letter)
 #******************************************************************************

#task3
def mystery():
    results = {
    'sanity': 'Hello'}
    return results
#******************************************************************************
#task4
def divide_numbers(x,y):
    return x / y
  
#******************************************************************************
#task5
def check(a, x):
    return x in a
#******************************************************************************
#task6
class Sleigh(object):
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'
      
#******************************************************************************
#task7
def positive_sum(arr):
    sum = 0
    for i in arr:
        if i>0:
            sum+=i
    return sum
#******************************************************************************
#task8
def count_consonants(text):
    s = set()
    for i in text.lower():
        if i.isalpha():
            s.add(i)
    return len(s - {"a", "e", "i", "o", "u"})
#******************************************************************************

#task9
def highest_value(a, b):
    sum_a, sum_b = 0, 0
    for i in a:
        sum_a+=ord(i)
    for i in b:
        sum_b+=ord(i)
    return a if sum_a==max(sum_a,sum_b) else b
#******************************************************************************

#task10
def single_digit(n):
    sum = 0
    if n > 9:
        while n != 0:
            sum += (n % 2)
            n = n//2
        return sum if sum < 10 else single_digit(sum)
    else: return n
