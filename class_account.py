#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:12:40 2024

@author: jacquesaoustin
"""

class book:
    
    """ THis is the class to store books"""
    
    def __init__ (self, title, year, author):
        
        self.title = title
        self.year = year
        self.author = author
    
class friend:
    
    """This is a class to store the infos about my friends"""
    
    def __init__ (self, name,library = None):
        
        """ For now check the name but later on ADD DATE AND PASSWORD"""
        
        self.name = name
        self.library = library
        
        if self.library is None:
            self.library = []        
        else:
            self.library = library
        
    def add_book(self,book):
            
        self.library.append(book)
        
    def del_book(self,title):
        
        for book in self.library:
            if book.title == title:
                self.library.remove(book)
            
            
    
        
        
