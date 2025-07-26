class Solution:
    def interpret(self, command: str) -> str:
        goal_list = []
        command_len = len(command)
        i = 0
        result = '' 
        while i < command_len:
            if command[i] == 'G':
                result += 'G'
                i += 1
            elif command[i:i+2] == '()':
                result += 'o'
                i += 2
            elif command[i:i+4] == '(al)':
                result += 'al'
                i += 4
        return result

