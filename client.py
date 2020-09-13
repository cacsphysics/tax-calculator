#############################
"""
    Client Class
"""
#############################
from .taxes import Taxes

class Client:
    """
        Client class
    """
    def __init__(self, income, file_status):
        self.income = income
        self.file_status = file_status
        self.taxes = Taxes(self, income, file_status)
    
    ################   Set Functions   ################
    def set_Income(self, income):
        self.income = income
    def set_FileStatue(self, file_status):
        self.file_status = file_status
    
        

    
    