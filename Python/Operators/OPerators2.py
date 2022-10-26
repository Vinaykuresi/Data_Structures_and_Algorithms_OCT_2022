Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = 45
>>> num2 = 35
>>> num3 = 25
>>> 
>>> num1 += num3
>>> 
>>> num1
70
>>> # num1 = num1 + num3
>>> 
>>> 
>>> num2 *= (num3-20)
>>> num2
175
>>> 
>>> num3 %= ((num2-num1)/5)
>>> num3
4.0
>>> 
>>> (num2/5 > num3) and (num1-20 < num2/15)
False
>>> 
>>> 
>>> (num2/5 < num3) or (num1-20 > num2/15)
True
>>> 
>>> ((num1/(num2%10) + 23) <= num3) or not((num3+10)/(num1/5) > 4)
True
>>> ((num1/(num2%10) + 23) <= num3)
False
>>> not((num3+10)/(num1/5) > 4)
True
>>> False or True
True
