# theater.py
#
# The owner of a monopolistic movie theater in a small town has
# complete freedom in setting ticket prices.  The more he charges, the
# fewer people can afford tickets.  The less he charges, the more it
# costs to run a show because attendance goes up.  In a recent
# experiment the owner determined a relationship between the price of
# a ticket and average attendance.
#
# At a price of $5.00/ticket, 120 people attend a performance.  For
# each 10-cent change in the ticket price, the average attendance
# changes by 15 people.  That is, if the owner charges $5.10, some 105
# people attend on the average; if the price goes down to $4.90,
# average attendance increases to 135.
#
# Unfortunately, the increased attendance also comes at an increased
# cost.  Every performance comes at a fixed cost of $180 to the owner
# plus a variable cost of $0.04 per attendee.
#
# The owner would like to know the exact relationship between profit
# and ticket price in order to maximize the profit.
#
# Write a program to figure out the best ticket price (to the nearest
# 10 cents) that maximizes profit.
#
# Credit: This problem comes from "How to Design Programs", 2nd Ed.
from decimal import *

def best_price(): 
    base_price = Decimal('5.0')
    base_attendance = Decimal('120')
    attendace_change = Decimal('15')
    price_change = Decimal('0.1')

    fixed_cost = Decimal('180')
    variable_cost_per_attendee = Decimal('0.04')
    start_price = Decimal('0.10')
    end_price = Decimal('10.00')

    # profit = revenuse - cost
    def revenue(price: float, attendees: int): 
        return price * attendees
    
    def cost(attendees: int): 
        return fixed_cost + variable_cost_per_attendee * attendees

    def profit(price: float):
        attendees = base_attendance + (base_price - price) / price_change * attendace_change
        return revenue(price, attendees) - cost(attendees)

    # so how do we iterate through prices?
    price = start_price
    best_price = price
    best_profit = profit(price)

    while price < end_price:
        price += price_change
        current_profit = profit(price)
        if(current_profit > best_profit):
            best_profit = current_profit
            best_price = price
    return best_price
    
print(f"Best price is ${best_price()}")

        