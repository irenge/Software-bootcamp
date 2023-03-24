"""
Create a new Python file in this folder called task3.py.

Design a program that determines the award a person competing in a
triathlon will receive.

Your program should read in the times in minutes for all three events of a
triathlon, namely swimming, cycling, and running, and then calculate and
display the total time taken to complete the triathlon.

The award a participant receives is based on the total time taken to
complete the triathlon. The qualifying time for awards is 100 minutes.
Display the award the participant will receive based on the following
criteria:
    """

x = int(input("Enter your swimming times in minutes : "))
y = int(input("Enter your cycling time: "))
z = int(input("Enter your running time: "))

time_taken = x + y + z

if time_taken <= 100:
    award = "Provincial colours"
elif time_taken <= 105:
    award = "Provincial Half Colours"
elif time_taken <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"
print(f"You got {award}")

