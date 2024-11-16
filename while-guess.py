# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:26:22 2024

@author: User
"""
import random #亂數

ans = random.randint(1, 100) # 請隨機取數，範圍為1~100正整數

guess = 0

while guess != ans:
    guess = int(input("請輸入0~100的值來猜數:"))
    
    if guess > ans:
        print("請猜小一點")
    if guess < ans:
        print("請猜大一點")
print("恭喜你，猜中了，答案是:",ans)
