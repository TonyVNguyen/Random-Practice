#Tony Nguyen

#Project Euler Problem 1

#find the sum of all the multiples of 3 or 5 below 1000

def answer1():
    answer = 0 #Initialize variables
    i = 0
    while i < 1000: #While it's still under below 1000
        if i % 3 == 0 or i % 5 == 0: #If it's a multiple of 3 or 5
            answer+= i  #Add the multiple of 3 or 5 to the accumulator
        i+=1            #Add to the counter

    return answer  #Returns 233168 and passes gets the checkmark on Project Euler!
