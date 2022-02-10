# Day 1 - Sonar Sweep
# Count the number of times a depth measurement increases from the previous measurement.
# There is no measurement before the first measurement.

# In this example, there are 7 measurements that are larger than the previous measurement:
# 199 (N/A - no previous measurement)
# 200 (increased)
# 208 (increased)
# 210 (increased)
# 200 (decreased)
# 207 (increased)
# 240 (increased)
# 269 (increased)
# 260 (decreased)
# 263 (increased)

# How many measurements are larger than the previous measurement?
# Input file: sonar_sweep_measurements.txt
# Submitted answer: 1393


from typing import TextIO


def sonar_sweep(input_file: TextIO):
    previous_sonar = int(input_file.readline().strip())
    total_larger_measurements = 0

    for line in input_file:
        current_sonar = int(line.strip())

        if current_sonar > previous_sonar:
            total_larger_measurements += 1

        previous_sonar = current_sonar

    print(total_larger_measurements)
    return total_larger_measurements


if __name__ == '__main__':
    with open('sonar_sweep_measurements.txt', 'r') as in_file:
        sonar_sweep(in_file)
