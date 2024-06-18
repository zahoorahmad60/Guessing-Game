# -*- coding: utf-8 -*-
"""Guessing Game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1txVNGmokL3dKJGC0iI7r3YXSALoXJccq
"""

import random

random_number = random.randint(0,100)
user_input = int(input("Guess The Number here"))       #taking input from user
i = 1
while(True):      #game loop
  if(random_number == user_input):    #condition if user guessed correctly
    print("You won")
    print(f"You guessed in these attempts: {i}")
    break    #terminating the loop
  elif(random_number > user_input):              #conditions to give user hints
    print("Guess greater")
    user_input = int(input("Guess The Number here"))
  elif(random_number < user_input):
    print("Guess lower")
    user_input = int(input("Guess The Number here"))
  i +=1
