# Day 1 part 2 - Sonar Sweep Sliding Sums
# Consider sums of a three-measurement sliding window.
# Count the number of times the sum of measurements increases from the previous sum.
# Stop when there aren't enough measurements left to create a new three-measurement sum.

# For example, the three-measurement sliding window looks like:
# 199  A
# 200  A B
# 208  A B C
# 210    B C D
# 200  E   C D
# 207  E F   D
# 240  E F G
# 269    F G H
# 260      G H
# 263        H

# Compare A with B, then compare B with C, then C with D, and so on
# In this example, there are 5 sums that are larger than the previous sum:
# A: 607 (N/A - no previous sum)
# B: 618 (increased)
# C: 618 (no change)
# D: 617 (decreased)
# E: 647 (increased)
# F: 716 (increased)
# G: 769 (increased)
# H: 792 (increased)

# How many sums are larger than the previous sum?
# Input file: sonar_sweep_measurements.txt
# Submitted answer: 1359


from typing import TextIO


def sonar_sweep_sliding_sums(input_file: TextIO):
    # Store the count of increased sums
    total_larger_sums = 0
    current_window = [0, 0, 0]

    # Read the first 3 inputs from the file into a list of strings
    previous_window = input_file.read(12).splitlines()

    # Convert list of strings to list of int
    for i in range(len(previous_window)):
        previous_window[i] = int(previous_window[i])

    for line in input_file:
        # Store the sum of the 3 previous inputs
        previous_sum = sum(previous_window)

        # Update the next window to include the last 2 inputs of previous window, and
        # Read the next line, strip, convert to int and assign it as the 3rd/final input
        current_window[0], current_window[1] = previous_window[1], previous_window[2]
        current_window[2] = int(line.strip())

        # Store the sum of the 3 next inputs
        current_sum = sum(current_window)

        # Compare sums: if the current sum is greater than the previous sum, increase count by 1
        if current_sum > previous_sum:
            total_larger_sums += 1

        # Reassign next window values to previous window, to be summed & compared on the next iteration
        previous_window = current_window

    print(total_larger_sums)


with open('sonar_sweep_measurements.txt', 'r') as in_file:
    sonar_sweep_sliding_sums(in_file)
