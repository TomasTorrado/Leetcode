from collections import defaultdict

# Approach: get count of every occurance of a character in a string and create a list hasmap where strings with the same count go together.
# Gotcha: You dont need to sort the strings against each other, use a hashmap to group them instead

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list) 
        for i in strs:
            count = [0] * 26 # mapping from a to z       

            for c in i:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(i)

        return result.values()