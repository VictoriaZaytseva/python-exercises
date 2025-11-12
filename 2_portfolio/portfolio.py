# portfolio.py
#
# This file contains a function that reads a CSV file of
# "name,shares,price" data into a list of dictionaries.  The file
# `report.py` uses this function.   We'll make some modifications
# in exercises below.

def read_portfolio(filename):
    '''
    Read a CSV file of name, shares, price data into a list of dicts.
    '''
    portfolio = [ ]
    with open(filename, "r") as file:
        # Skip the first line of headers
        next(file)
        for line in file:
            row = line.split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            holding = { 'name': name, 'shares': shares, 'price': price }
            portfolio.append(holding)
    return portfolio

# -----------------------------------------------------------------------------
# Exercise 1:  Classes vs. Dicts
#
# In the above code, a dictionary is used to represent a single record of
# data.  For example, in the line:
#
#          holding = { 'name': name, 'shares': shares, 'price': price }
#
# Instead of using a dictionary, what if you used a class instance?
# What core features would you give this new class?
#
# You first task is as follows:
#
#     1. Define a class to replace the holding dictionary.
#     2. Write a new version of read_portfolio() that uses this class.
#     3. Modify report.py as necessary to work with instances.
#
# Are there any parts of the `report.py` program that could be better
# organized as features of this newly defined class instead?  For
# example, should the class have any methods added to it?


# -----------------------------------------------------------------------------
# Exercise 2:  Classes vs. Containers
#
# In this code, a Python list is being used to represent a "Portfolio"
# of stock holdings.   Does it make any sense to use a custom Portfolio
# class for this instead?  If so, what would that class look like and
# what features should it support?
#
# Your task is as follows:
#
#    1. Define a Portfolio class that takes the place of a Python list.
#    2. Write a new version of read_portfolio() that creates this class.
#    3. Modify report.py as necessary to work with the data.
#
# Are there any parts of the `report.py` program could be better
# organized as features of the `Portfolio` class instead?  Note:
# we're going to keep the make_report() function separate.  That
# should NOT turn into a method.

class Portfolio:
    ...

# -----------------------------------------------------------------------------
# Exercise 3: Data Abstraction
#
# A core tenant of data abstraction is that applications are written to
# a specific programming interface and that internal implementation details
# don't matter so much.   Think about all of the different ways that
# fractions were implemented in Project 1.
#
# Suppose that you wanted to change the internal representation of data
# inside your Portfolio class to use pandas.   Pandas has a helpful function
# for reading a CSV file:
#
#       import pandas
#       data = pandas.read_csv('portfolio.csv')
#
# What modifications would you make to the Portfolio class to use
# pandas dataframes as an internal data representation format?
#
# Can you use the modified Portfolio class with the `report.py`
# program *WITHOUT* making any changes to the code in that file?
#
# Note: For this exercise, it make might sense to make a separate
# class PandasPortfolio.   Keep in mind that an instance of this class
# would be provided to the make_report() function in report.py.

class PandasPortfolio:
    ...

    
