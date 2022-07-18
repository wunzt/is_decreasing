# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/16/2022
# Description: Returns True if the list of numbers is strictly descending, via recursion. Otherwise, returns False.

def is_decreasing(num_list):
    """Returns True if the list of numbers is strictly descending. Otherwise, returns False."""

    if len(num_list) == 1:
        return True

    if num_list[0] > num_list[1]:
        return is_decreasing(num_list[1:])
    else:
        return False
