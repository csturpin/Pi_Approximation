#Pi Approximation Formula: pi/4 = (1/1 - 1/3 + 1/5 -1/7 + 1/9 - 1/11 + 1/13 ...)

#The user specifies the number of iterations to be used in the formula here
NUM = input("Enter Number of Iterations: ")

#i is the current iteration in the series in the formula; it starts at 1
#j is the denominator of each fraction in the series in the formula; it starts as 1
#summ is the sum of all of the fractions in the series in the formula
i = 1
j = 1
summ = 0

print "\n%10s%20s" % ("Iteration", "Pi Approximation")
print "%10s%20s" % ("=========", "================")

#This loop repeats as long as i is less than or equal to the total number of iterations specified by the user
while i <= NUM:
    
    #If the current iteration is even, the fraction in the series is negative
    if i%2 == 0:
        summ -= 1.0/j
    #If the current iteration is odd, the fraction in the series is positive
    else:
        summ += 1.0/j

    #The sum of the series in the formula is equal to pi divided by 4, so pi is equal to the sum of the series multiplied by 4
    pi = 4*summ

    print "%10d%20.12f" % (i, pi)

    #The iteration i increases by 1 each time; the denominator j increases by 2 each time (so it is always odd since it starts as 1)
    i += 1
    j += 2

print "\nThe approximate value of pi is: ", pi
print "\n\n"

#The known value of pi is roughly approached (accurate to two decimal places) around an input NUM value of 1000; accuracy increases as iterations do
