## Importing an entire module

## To import an entire Python Standard Library module, you use the import keyword. The import keyword searches for a module or library in a system and adds it to the local Python environment. After import, specify the name of the module to import. For example, you can specify import statistics to import the statistics module. This will import all the functions inside of the statistics module for use later in your code. use the mean() function from the statistics module to calculate the average number of failed login attempts per month for a particular user. In the following code block, the total number of failed login attempts for each of the twelve months is stored in a list called monthly_failed_attempts. Run this code and analyze how mean() can be used to calculate the average of these monthly failed login totals and store it in mean_failed_attempts

import statistics
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
mean_failed_attempts = statistics.mean(monthly_failed_attempts)
print("mean:", mean_failed_attempts)

import statistics
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
median_failed_attempts = statistics.median(monthly_failed_attempts)
print("median:", median_failed_attempts)






## Importing specific functions from a module

## To import a specific function from the Python Standard Library, you can use the from keyword. For example, if you want to import just the median() function from the statistics module, you can write from statistics import median. To import multiple functions from a module, you can separate the functions you want to import with a comma. For instance, from statistics import mean, median imports both the mean() and the median() functions from the statistics module.

from statistics import mean, median
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
mean_failed_attempts = mean(monthly_failed_attempts)
print("mean:", mean_failed_attempts)
median_failed_attempts = median(monthly_failed_attempts)
print("median:", median_failed_attempts)
