class Student:                                  #creating a class for saving all student info in 1 object
    def __init__(self,id,first,last,major):     # creating the object
        self.id=id
        self.first=first
        self.last=last
        self.major=major
        self.email=str(id)+'@students.liu.edu.lb'       # you can change the email for whatever you want

    def allinfo(self):      #method to list all the students information                        
        return 'ID={} , First_Name={} ,Last_Name={}, Major in {}, Email={}'.format(self.id,self.first,self.last,self.major,self.email)
std_list = [] 










