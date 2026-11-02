marks = int(input("Enter your marks:  "))

if (marks > 100):
    print(" Marks should be 100/N ")

elif (marks > 90):
    print("A+")
elif (marks > 80):
    print("A")
elif (marks > 60):
    print("B")
elif (marks > 50):
    print("C")
else:
    print("Better luck Next Time")