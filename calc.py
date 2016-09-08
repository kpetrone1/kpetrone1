print((42*60)+42)

print((10)*(1/1.61))

print((((42*60)+42)/(10*(1/1.61)))/60)

print(((42*60)+42)/(10*(1/1.61)))

print((10*(1/1.61))/((42 + (42/1)*(1/60))*(1/60)))


#Homework from Session 2
print('\n')
print('Question 1: Volume of a Sphere with Radius = 5')
print('Volume of sphere = (4/3)*3.1415926*(r**3)')
radius = 5
print('Volume of sphere = ', (4/3)*3.1415926*(radius**3))
print('\n')
print('Question 2: Total Wholesale Cost of Sixty Copies')
print('Total Wholesale Cost of Sixty Copies = Cost of Books + Cost of Shipping')
print('Cost of Books = Cover Price Per Book * (1-Discount) * Number of Copies')
Cover_Price_Per_Book = 24.95
Discount = .40
Number_of_Copies = 60
Cost_of_Books = Cover_Price_Per_Book*(1-Discount)*Number_of_Copies
print('Cost of Books = ', Cost_of_Books)
print('Cost of Shipping = Shipping Cost of First Copy + (Shipping Cost Per Additional Copy * (Total Number of Copies - 1))')
Shipping_Cost_of_First_Copy = 3
Shipping_Cost_Per_Additional_Copy = 0.75
Total_Number_of_Copies = 60
Cost_of_Shipping = Shipping_Cost_of_First_Copy + (Shipping_Cost_Per_Additional_Copy*(Total_Number_of_Copies-1))
print('Cost of Shipping = ', Cost_of_Shipping)
print('Total Wholesale Cost of Sixty Copies = Cost of Books + Cost of Shipping')
Total_Wholesale_Cost_of_Sixty_Copies = Cost_of_Books + Cost_of_Shipping
print('Total Wholesale Cost of Sixty Copies = %.2f' % Total_Wholesale_Cost_of_Sixty_Copies)
print('\n')
print('Question 3: Return Time for Breakfast')
print('Departure Time: 6:52am')
print('Time Zero: 12:00am')
print('"Number of Seconds From Time Zero to Departure Time" = Number of Seconds from 12:00am to 6:52am')
print('Number of Seconds From Time Zero to Departure Time = 6*60*60 + 52*60')
Number_of_Seconds_From_Time_Zero_to_Departure_Time=((6*60*60)+(52*60))
print('Total Length of Run in Seconds = Length of Phase 1 in Seconds + Length of Phase 2 in Seconds + Length of Phase 3 in Seconds')
print('Example Calculation: Length of Phase 2 in Seconds = number of miles * pace per mile in seconds = (3 miles) * ((7 minutes * 60 seconds) + 12 seconds)')
Length_of_Phase_1_in_Seconds = (1)*((8*60)+15)
print('Length of Phase 1 in Seconds = ', Length_of_Phase_1_in_Seconds)
Length_of_Phase_2_in_Seconds = (3)*((7*60)+12)
print('Length of Phase 2 in Seconds = ', Length_of_Phase_2_in_Seconds)
Length_of_Phase_3_in_Seconds = (1)*((8*60)+15)
print('Length of Phase 3 in Seconds = ', Length_of_Phase_3_in_Seconds)
Total_Length_of_Run_in_Seconds = Length_of_Phase_1_in_Seconds + Length_of_Phase_2_in_Seconds + Length_of_Phase_3_in_Seconds
print('Total Length of Run in Seconds = ', Total_Length_of_Run_in_Seconds)
Number_of_Seconds_From_Time_Zero_to_Return_Time_From_Run = Number_of_Seconds_From_Time_Zero_to_Departure_Time + Total_Length_of_Run_in_Seconds
print('Number of Seconds From Time Zero to Return Time From Run = ', Number_of_Seconds_From_Time_Zero_to_Departure_Time + Total_Length_of_Run_in_Seconds)
Number_of_Minutes_From_Time_Zero_to_Return_Time_From_Run = Number_of_Seconds_From_Time_Zero_to_Return_Time_From_Run/60
print('Number of Minutes From Time Zero to Return Time From Run = ', Number_of_Minutes_From_Time_Zero_to_Return_Time_From_Run)
Number_of_Hours_From_Time_Zero_to_Return_Time_From_Run = Number_of_Minutes_From_Time_Zero_to_Return_Time_From_Run/60
print('Number of Hours From Time Zero to Return Time From Run = ', Number_of_Hours_From_Time_Zero_to_Return_Time_From_Run)
Number_of_Minutes_in_Remainder_of_Hours_Calculation = Number_of_Minutes_From_Time_Zero_to_Return_Time_From_Run % 60
print('Number of Minutes in Remainder of Hours Calculation = ', Number_of_Minutes_in_Remainder_of_Hours_Calculation)
print('Final Answer for Question 3: The time at which the runner returns to his or her house for breakfast is 7 hours and 30 minutes from time zero, or 12:00 am. Thus, the runner\'s return time is 7:30 am.')
print('\n')
print('Question 4: Average Grade Increase')
Grade_1 = 82
print('Grade 1 = ', Grade_1)
Grade_2 = 89
print('Grade 2 = ', Grade_2)
Percentage_Increase_From_Grade_1_to_Grade_2 = ((Grade_2-Grade_1)/Grade_1)*100
print('Percentage Increase From Grade 1 to Grade 2 = %.1f%%' % Percentage_Increase_From_Grade_1_to_Grade_2)

 
