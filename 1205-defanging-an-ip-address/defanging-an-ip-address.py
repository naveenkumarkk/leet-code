class Solution:
    def defangIPaddr(self, address: str) -> str:
        temp_address = ''
        for i in range(len(address)):
            if address[i] == '.':
                temp_address += '[.]'
            else:
                temp_address += address[i]
        return temp_address

