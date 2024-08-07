import re

def find_vowel_substrings(s, k):
    vowels = 'AEIOUaeiou'
    consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
    pattern = r'(?<=[%s])([%s]{%d,})(?=[%s])' % (consonants, vowels, k, consonants)
    
    matches = re.finditer(pattern, s)
    found_match = False
    
    for match in matches:
        substring = match.group()
        print(substring)
        found_match = True
    
    if not found_match:
        print(-1)

# Reading input from standard input (you may adjust this part based on how you're testing it)
if __name__ == "__main__":
    s = input().strip()
    find_vowel_substrings(s, 2)  # Assuming the minimum length required is 2 vowels