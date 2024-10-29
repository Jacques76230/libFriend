#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 07:30:17 2024

@author: jacquesaoustin
"""


import yaml

from class_account import friend,book

customer = friend('Jacques')
customer.add_book(book('patate',1998,'jean Pierre'))
customer.add_book(book('garde la peche', 1432, 'Aymar de la Pierre'))

customer2 = friend('Michel')
customer2.add_book(book('la fete',2003,'rita'))
customer2.add_book(book(' ecrire en anglais', 3445, ' xu7543'))
customer2.del_book('la fete')


with open('library.yaml','w') as file:

    data = {'customer':customer.name, 'book': [rere.title for rere in customer.library], 'year': [book.year for book in customer.library]}
    yaml.dump(data,file)