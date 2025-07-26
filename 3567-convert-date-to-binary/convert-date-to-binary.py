class Solution:
    def convertDateToBinary(self, date: str) -> str:

        date_list = date.split("-")
        binary_date = ''
        for key,value in enumerate(date_list):
            b = ''
            value = int(value)
            while value > 0:
                b = str(value%2) + b
                value//=2
            
            binary_date = binary_date + b
            if key != 2:
                binary_date = binary_date + '-'
        return binary_date
                
            
            

        
        