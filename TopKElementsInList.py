class Solution:

    # Time Complexity O(n long(n)) due to having to sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        sorted_freq = sorted(freq.items(), key=lambda item:item[1], reverse=True)
        
        return_list = [i[0] for i in sorted_freq[:k]]
        return return_list

    # Time Complexity O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_list = [[] for i in range(0, len(nums)+1)]
        freq = {}

        # Count Frequency where key is number and value is frequency
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        # In a list add number to a list at index = frequency
        for key, value in freq.items():
            freq_list[value].append(key)
                             
        return_list = []

        # Counting from highest possible frequency, add number to a list until asked number of numbers are matched
        for i in range(len(freq_list)-1, 0, -1):
            for j in freq_list[i]:
                return_list.append(j)
                if len(return_list) == k:
                    return return_list
        
