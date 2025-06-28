'''
        Design and implement a TwoSum class. It should support the following
        operations: add and find.
        add - Add the number to an internal data structure. find - Find if there exists any
        pair of numbers which sum is equal to the value.
        For example, add(1); add(3); add(5); find(4) -> true find(7) -> false
        URL: https://leetcode.com/problems/two-sum-iii-data-structure-design/

'''

import collections


class TwoSum(object):
    def __init__(self):
        """
            initialize your data structure here
        """

        self.__num_list = collections.defaultdict(int) # this is used to the value only in the in

        '''
            In Python, defaultdict is a subclass of the built-in dict class in the collections module. 
            It provides a default value for a nonexistent key, so you don’t get a KeyError.

            from collections import defaultdict

            d = defaultdict(default_factory)

            default_factory is a function that provides the default value (e.g., int, list, str).
        '''

    def add(self,num):
        """ 
            Add the number to an internal data structure.
            :rtype: nothing
        """
        
        self.__num_list[num] += 1
    
    def find(self,value):

        """
            Find if there exists any pair of numbers which sum is equal to the value.
            :type value: int
            :rtype: bool
        """
        if len(self.__num_list) == 0:
            return False
        else:
            for key in self.__num_list.keys():
                target = value - key
                if ( target != key and target in self.__num_list)  or (target == key and self.__num_list[target] >1 ):
                    return True
            return False
        
if __name__ == "__main__":

    # Your TwoSum object will be instantiated and called as such

    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    param2 = obj.find(4)
    print("Found sum of 4:", param2)

    param2 = obj.find(7)
    print("Found sum of 7:", param2)


