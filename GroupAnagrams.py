class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_string = {}
        # Sort strings alphabetically and use it as a key
        for s in strs:
            temp = ''.join(sorted(s))
            if temp in output_string:
                output_string[temp].append(s)
            else:
                output_string[temp]=[s]
        
        
        return_list = []
        for v in output_string.values():
            return_list.append(v)

        # Above block can be replaced by list(output_string.values())
        return return_list
