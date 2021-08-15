from mypack.scholar import student

class disability(student):
    def __init__(self, percentage,marks,category):
        self.dis_per = percentage
        self.marks = marks
        self.category = category
        
    def disable(self):
        scholar = self.scholar()
        p=0
        if (self.dis_per > 50.0):
            p=10
            total_fee = 40000
            scholar_d = (total_fee/100) * p
        total_sch = scholar_d + scholar
        return total_sch

marks = float(input("Enter the marks in percentage : "))

while(True):
    category = str(input("Enter the category of the student(res or ur) : "))
    if(category != str("res") and category != str("ur")):
        print("input only 'res' or 'ur is accepted'")
    else:
        break
    
disability_p = float(input("Enter the disability percentage of student : "))

scholarship_disable = disability(disability_p,marks,category)

scholarship = str(scholarship_disable.disable())
 
print("The Student's Scholarship is : "+scholarship)
