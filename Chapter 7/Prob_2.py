# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

m1 = int(input("Enter the marks in subject 1 :"))
m2 = int(input("Enter the marks in subject 2 :"))
m3 = int(input("Enter the marks in subject 3 :"))

# Check for total percentage
total_percentage = ((m1 + m2 + m3)*100) / 300
print("Total percentage is : ", total_percentage)

if (total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("Student has passed", total_percentage)
else:
    print("Student has failed ! Try again next year", total_percentage)

# # Check for marks in each subject
# if (m1>=33 and m2>=33 and m3<=33):
#     print("Student has passed", m1, m2, m3)
# else:
#     print("Student has failed", m1, m2, m3)