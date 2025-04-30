class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        # Encode each string, pre-pend by length number and delimeter # to end the number and start of the string
        for s in strs:
            output += str(len(s))
            output += "#" + s
        
        
        return output

    def decode(self, s: str) -> List[str]:

        return_list = []
             
        i, j = 0, 0
        
        while i < len(s):
            if s[j] == '#':
                num = int(s[i:j])
                
                return_list.append(s[j+1:j+1+num])
        
                i = j + num + 1
                j = i
            else:
                j += 1

        return return_list
            


            



