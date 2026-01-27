These are solutions for day 2 of 2025's Advent of Code competition. The problem description can be found at https://adventofcode.com/2025/day/2

But to summarize, the goal is to find the sum of all numbers within given ranges that have a repeated pattern of digits. For example, 4544-4546 would have 4545 as a valid repeated pattern of digits (45)(45). 

The input is a series of ranges in csv format, for example the input xxxx-yyyy, zzzzzzz-aaaaaaaa would refer to two ranges from xxxx to yyyy and zzzzzzz to aaaaaaaa that must be searched for repeated values. The highest number range is 12 digits long, while the lowest is 2. (22-99) and (123456789999-123456799999) for example
Submission 1 looks for values that are repeated only twice, and submission 2 looks for values that are repeated any number of times.

These solutions do not perform a brute search on each value in the range, rather it generates a list of all possible patterened values within that range based on the number of times a pattern could be repeated given the number of digits in the range, then sums that value, reducing the computational need.

This is done by breaking down the range into the possible prime-value length subsets of characters in the range, and incrementing between the low and high value of the range, adding the value if applicable, and ignoring a value if it has already been counted.
eg: 123456-678910. For this range, the factored value lengthed subsets are 1,2,3,6. We ignore 6, as in order for a pattern to be repeated, the length of the pattern must at most be half the length of the entire value. This leaves us with sublengths of 1, 2 and 3. For pattern lengths of 1, valid candidates are 111111,222222,333333,444444,555555,666666,777777,888888,999999, and we only add the values 2-6, as those are the only candidates in the given range. Moving on to two, we have 10,11,12,13,14,15,16.......97,98,99, of which only 12->67 are within the range (121212.....676767), taking care to pass over the already counted 22,33,44... And we perform the same process with repeated patterns of lenght 3. 

Helper functions were created to perform these counts based on the fraction of the range evenly divisible by the length. (halves, thirds, fifths, sevenths) and calculated for the appropriate ranges.
