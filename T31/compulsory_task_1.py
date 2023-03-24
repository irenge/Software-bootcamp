"""
Compulsory Task 1: 
------------------

Copy the code provided below to a new file named compulsory_task_1.py: 
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Cape Town"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
    def location(self):
        print(self.head_office_location)

class OOPCourse(Course):
    description = "OOP Fundamentals"
    trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print(f"Course: {self.description} \nTrainer:  {self.trainer}")
    def show_course_id(self):
        print("Course ID: #12345")
course1 = OOPCourse()
course1.contact_details()
course1.trainer_details()
course1.show_course_id()

