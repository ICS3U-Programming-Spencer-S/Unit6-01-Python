#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Dec 19, 2022
# A program which uses lists to generate 10 numbers
# with a range of 1/100 and find the average


import random


def main():

    # intro message
    print("This is a program that generates 10 numbers and finds the average")
    print("")

    # creates an empty list and sum
    list_num = []
    sum = 0

    # for loop in range of 10 as it needs 10 numbers
    for counter in range(10):
        # creates a number from 0-100
        random_num = random.randint(0, 100)
        # displays number was added to list
        print(f"{random_num} was added to the list")
        # appends the number to the list
        list_num.append(random_num)

    # for loop in range of 10 that calculates the sum of the past 10 numbers
    for counter in range(10):
        sum += list_num[counter]

    average = sum / 10
    # output message
    print("")
    print(f"The average of {list_num} is {average}")


if __name__ == "__main__":
    main()
