#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 12, 2023
# This program generates 10 random numbers then finds the average and uses lists.

import constants
import random


def main():
    # introduce program to user
    print("Hello, this program generates 10 random numbers then finds the average.")

    # declare list
    average_list = []

    # initialize sum
    sum = 0

    # populate list with loop
    for counter in range(0, constants.SIZE):
        # generate random number 0-100
        random_number = random.randint(constants.MIN, constants.MAX)

        # populate list
        average_list.append(random_number)

    # calculate average
    for counter_two in range(0, constants.SIZE):
        # calculate sum
        sum = sum + average_list[counter_two]

    # calculate average
    average = sum / 10

    # display sum
    print("The average is {}.".format(average))


if __name__ == "__main__":
    main()
