###############################################
"""
    Taxes Class
    Currently the focus is federal income tax
"""
###############################################


class Taxes:
    """
        taxes class
    """
    def __init__(self, income, file_status):
        """
            Setting up instance parameters
        """
        self.income = income
        self.file_status = file_status
        self.indicator = None
        self.bracket = None
        self.marginal_Tax = None
        self.tax = None
        self.effective_IncomeTax = None
    
    
    ################   Set Functions   ################
    def set_Income(self, income):
        self.income = income
    def set_FileStatue(self, file_status):
        self.file_status = file_status
      
    def federal_Bracket(self):
        """
            Function for current federal tax brackets
        """
        if (self.indicator) == 's':
            self.bracket = [
                [0, 9875, 0.1],
                [9876, 40125, 0.12],
                [40126, 85525, 0.22],
                [85526, 163300, 0.24],
                [163301, 207350, 0.32],
                [207351, 518400, 0.35],
                [518401, float('nan'), 0.37]
            ]
        elif (self.indicator) == 'mfj':
            self.bracket = [
                [0, 19750, 0.1],
                [19751, 80250, 0.12],
                [80251, 171050, 0.22],
                [171051, 326600, 0.24],
                [326601, 414700, 0.32],
                [414701, 622050, 0.35],
                [622051, float('nan'), 0.37]
            ]
        elif (self.indicator) == 'mfs':
            self.bracket = [
                [0, 9875, 0.1],
                [9876, 40125, 0.12],
                [40126, 85525, 0.22],
                [85526, 163300, 0.24],
                [163301, 207350, 0.32],
                [207351, 311025, 0.35],
                [311026, float('nan'), 0.37]
            ]
        elif (self.indicator) == 'shh':
            self.bracket = [
                [0, 14100, 0.1],
                [14101, 53700, 0.12],
                [53701, 85500, 0.22],
                [85501, 163300, 0.24],
                [163301, 207350, 0.32],
                [207351, 518400, 0.35],
                [518401, float('nan'), 0.37]
            ]
        
    def status_Indicator(self):
        """
            This is planned to be a temporary function for a future input variable
        """
        status_Options = {
            'single':'s',
            'married filing jointly':'mfj',
            'married filing separately':'mfs',
            'single head of household':'shh'
        }
        self.indicator = status_Options.get(self.file_status, 'unknown')

    def tax_Calculate(self):
        
        if (self.bracket == None):
            self.federal_Bracket()
        else:
            pass
        
        if (self.marginal_Tax == None):
            self.get_MarginalTax()
        else:
            pass
        
        bracket = self.bracket
        income = self.income
        
        tax = 0
        i = 0
        while (bracket[i][2] <= self.marginal_Tax):
           current_Bracket = bracket[i]
           i += 1
           if ((current_Bracket[1] - income) <= 0):
               tax += (current_Bracket[1] - current_Bracket[0])*current_Bracket[2]
           else:
               tax += (income - current_Bracket[0])*current_Bracket[2]
            
        self.tax = tax
    
    def  get_MarginalTax(self):
        
        bracket = self.bracket
        income = self.income
        
        for level in bracket:
            if ((level[0] < income) and income < level[1]):
                self.marginal_Tax = level[2]
        
        return self.marginal_Tax
                
    def get_EffectiveIncomeTax(self):
        
        income = self.income
        if (self.tax == None):
            self.tax_Calculate()
        else:
            pass
        tax = self.tax
        self.effective_Tax = round(tax/income, 2)
        
        return round(tax/income, 2)