"Data Encapsulation"
class student:
    def __init__(self,name,roll_number,password):
        self.name=name #Public attribute
        self._roll_number=roll_number #Protected attribute
        self.__password=password #Private attribute
    def display_details(self):
        


    def get_password(self,new_password):
        return self.__password