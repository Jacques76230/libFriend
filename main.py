#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:20:28 2024

@author: jacquesaoustin
"""


from class_account import friend,book

print('Isn it your first visit?')
answer1 = input().lower()

if answer1 == 'yes':
    
    print ('Could you give me your name?')
    names = friend(input())
    
    print('Add books')
    
    