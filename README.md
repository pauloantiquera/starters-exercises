# Programming Exercises List

This exercises list purpose is for you, starters, work out your programming skills. All exercises in this list require a function creation in Python. For each exercise, you should provide two source code files. Into one of the files (.py), you will code the function that solves the given problem. The content of the second file (.test.py) will be the unit test cases that cover all the exercise requirements.

## 1. Leap Year problem

Write a function that receives a year as a parameter and returns True if the given year is a leap year. The function should return False for a provided year that isn't a leap year. In the following, the algorithm to define whether a year is a leap year or not:

```
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year) 
```