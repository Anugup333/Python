''' Date- 27/01/2024
Compare two string  but this program`s Complexity is o(n)'''

def sort_string_with_dict(input_string):
    char_freq = {}
    for char in input_string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    sorted_string = ''.join([char * char_freq[char] for char in sorted(char_freq.keys())])
    return sorted_string

def isAnagram(str1, str2) :
	# write your code here.
	str1 = sort_string_with_dict(str1)
	str2 = sort_string_with_dict(str2)
	if str1 == str2:
		return True
	else:
		return False
