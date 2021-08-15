class student(object):
    def __init__(self, marks, category):
        self.marks = marks
        self.category = category
        
    def scholar(self):
        p = 0
        total_fee = 40000
        scholarship = 0
        if(self.marks >= 90.0):
            scholarship = (40000/100) * 15
        elif(self.marks >75.0 and self.category == "res"):
            scholarship = (40000/100) * 10
        return scholarship
        
            
    
