#Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
Total = 1
#A. Write a loop that prints each of the numbers on a new line.
#for number in xs:
    #print(number)
#B. Write a loop that prints each number and its square on a new line.
#for number in xs:
    #print(number)
    #sq = number ** 2
    #print(sq)
#C. Write a loop that adds all the numbers from the list into a variable called total. You should set the total variable to have the value 0 before you start adding them up, and print the value in total after the loop has completed.
#for number in xs:
#    Total = number + Total
#print(Total)
#D. Print the product of all the numbers in the list. (product means all multiplied together)
for number in xs:
    Total = number * Total
print(Total)

